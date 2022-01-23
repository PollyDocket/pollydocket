"""Docket PDF Parser.

Provides functions to parse dockets. Parsed dockets are `dicts` containing the
data in the sections of the pdf (e.g. Status Information, Case Information,
etc.)
"""
import re
from typing import Callable, Dict, List, Tuple, Union

import pdfplumber
from pdfplumber.page import CroppedPage, Page

from . import utils

Page = Union[Page, CroppedPage]

# Constant height of bottom material not needed for parsing
BOTTOM_HEIGHT: float = 128.0


def parse_pdf(path: str) -> Dict:
    """Parse the pdf to a dict.

    Splits the pdf into sections deliniated by section headers. These sections
    are then passed to their corresponding parsers.

    Args:
        path: path to pdf to parse

    Returns:
        Dict: Dict of parsed pdf with sections as top-level keys
    """
    parsers: Dict[str, Callable] = {
        "Case Information": parse_case_info,
        "Status Information": parse_status_info,
        "Calendar Events": parse_cal_events,
        "Defendant Information": parse_defendant_info,
        "Case Participants": parse_case_participants,
        "Bail": parse_bail,
        "Charges": parse_charges,
        "Docket Entry Information": parse_docket_entry_info,
    }

    with pdfplumber.open(path) as pdf:
        pages = pdf.pages
        headings = get_headings(pages)

    sections = split_pages(pages, headings)

    ret = {}
    for sect, page in sections.items():
        if sect != "Docket":  # Don't care about the "docket" section
            ret[sect] = parsers[sect](page)

    return ret


def get_headings(pages: List[Page]) -> List[List[Dict]]:
    """Gets section headings.

    Gets section headings including their metadata (e.g. fontsize, bounding
    box). Each element of the returned list is all the headings on a single
    page.

    Args:
        pages: PDF pages

    Returns:
        List[List[Dict]]: List of section headings per page
    """
    headings = []
    for page in pages:
        words = page.extract_words(keep_blank_chars=True, extra_attrs=["size"])
        headings.append(
            [
                w
                for w in words
                if (w["text"].isupper() and w["size"] > 8.5 and w["size"] < 12)
            ]
        )

    return headings


def split_pages(
    pages: List[Page], headings_by_page: List[List[Dict]]
) -> Dict[str, Page]:
    """Splits pages based on their section headings.

    Args:
        pages: PDF pages
        headings_by_page: All headings in a pdf separated by page (e.g. returned
            from get_headings)

    Returns:
        Dict: keys are section headings, values are `CroppedPage`
    """
    sects = {}
    for page, headings in zip(pages, headings_by_page):
        pairs = list(utils.pairwise(headings))

        for pair in pairs:
            # Handles case where two headings are in a header bar
            # (e.g. Commonwealth Information --- Attorney Information)
            if pair[1]["bottom"] - pair[0]["bottom"] < 1:
                continue
            bbox = calc_bbox(page, pair[0], pair[1])
            sects[str.title(pair[0]["text"])] = page.within_bbox(bbox)

        last = pairs[-1][1]
        bbox = (0, last["bottom"], page.width, page.height - BOTTOM_HEIGHT)
        sects[str.title(last["text"])] = page.within_bbox(bbox)

    return sects


def calc_bbox(page: Page, h1: Dict, h2: Dict) -> Tuple:
    """Gets bounding box between two headings.

    Args:
        page: PDF page
        h1: First heading. Must be above `h2`
        h2: Second heading

    Returns:
        Tuple: Bounding box (left, top, right, bottom)
    """
    return (0, h1["bottom"], page.width, h2["top"])


def get_column(words: List, head: Dict) -> List:
    """Finds members of a column members.

    Finds column members by finding all words in `words` that have (roughly)
    the same x0 value as `head`

    Args:
        words: List of word objects
        head: Column heading object

    Returns:
        List: Cells of the column
    """
    rows = []
    left = head["x0"]
    for word in words:
        if abs(word["x0"] - left) < 0.5:
            rows.append(word)

    return rows


def split_page_by_x(page: Page, splits: Union[float, List[float]]) -> List:
    """Split page at `locs`.

    Splits a page at the x coordinates in `locs`

    Args:
        page: PDF Page (or CroppedPage)
        splits: List of x locations to split `page` at

    Returns:
        List: List of CroppedPage
    """
    # Since we're bounding with pairs, the first pair has to contain the left
    # edge and the last pair has to contain the right edge
    splits = [splits] if isinstance(splits, float) else splits
    locs = [0.0] + splits + [page.width]
    sects = []
    pairs = utils.pairwise(locs)
    for pair in pairs:
        bbox = (pair[0], page.bbox[1], pair[1], page.bbox[3])
        sects.append(page.within_bbox(bbox))

    return sects


def parse_case_info(page: Page, pad: float = 10.0) -> Dict:
    """Parse Case Information section.

    Args:
        page: PDF Page. Should be cropped to only contain Case Information
        pad: Optional. Adjusts the split to the left

    Returns:
        Dict: Parsed case information
    """
    # FIXME: Breaks if >2 things on one line (e.g. OTN/LOTN)
    # FIXME: Breaks if line wraps
    # FIXME: Breaks on CP Criminal Docket (Case Local info)
    texts = []
    pat = re.compile(r"([\s\S]+):\s?(.*)")
    splits = split_page_by_x(page, page.width // 2 - pad)
    texts += splits[0].extract_text(keep_blank_chars=True).splitlines()
    texts += splits[1].extract_text(keep_blank_chars=True).splitlines()

    ret = {}
    for text in texts:
        search = re.search(pat, text)
        if search is None:
            continue

        ret[search.group(1).strip()] = search.group(2).strip()

    return ret


def parse_status_info(page: Page) -> Dict:
    """Parse Status Information section.

    Args:
        page: PDF Page. Should be cropped to only contain Status Information

    Returns:
        Dict: Parse status information
    """
    words = page.extract_words(keep_blank_chars=True)
    status_info: Dict = {}

    # Every docket with status info has these two columns. Everything else is
    # key-value (or close enough)
    status_date = next((w for w in words if w["text"] == "Status Date"))
    status_date_col = get_column(words, status_date)

    proc_status = next((w for w in words if w["text"] == "Processing Status"))
    proc_status_col = get_column(words, proc_status)

    # Ignore column headings
    for date, status in zip(status_date_col[1:], proc_status_col[1:]):
        if "Items" not in status_info:
            status_info["Items"] = []
        status_info["Items"].append({"Date": date["text"], "Status": status["text"]})

    kvs = [w for w in words if w not in status_date_col + proc_status_col]
    # Sort by `bottom` to get all words on the same line,
    # then by `x0` to get in order from left-to-right.
    kv_iter = iter(sorted(kvs, key=lambda w: (w["bottom"], w["x0"])))
    for val in kv_iter:
        status_info[val["text"].replace(":", "")] = next(kv_iter)["text"]

    return status_info


def parse_cal_events(page: Page) -> Dict:
    return {}


def parse_defendant_info(page: Page) -> Dict:
    return {}


def parse_case_participants(page: Page) -> Dict:
    return {}


def parse_bail(page: Page) -> Dict:
    return {}


def parse_charges(page: Page) -> Dict:
    return {}


def parse_docket_entry_info(page: Page) -> Dict:
    return {}
