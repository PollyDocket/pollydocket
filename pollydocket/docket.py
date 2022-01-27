"""Docket PDF Parser.

Provides functions to parse dockets. Parsed dockets are `dicts` containing the
data in the sections of the pdf (e.g. Status Information, Case Information,
etc.)
"""
import re
from itertools import chain
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
        "Case Information": _parse_case_info,
        "Status Information": _parse_status_info,
        "Calendar Events": _parse_cal_events,
        "Defendant Information": _parse_defendant_info,
        "Case Participants": _parse_case_participants,
        "Bail": _parse_bail,
        "Charges": _parse_charges,
        "Docket Entry Information": _parse_docket_entry_info,
    }

    with pdfplumber.open(path) as pdf:
        pages = pdf.pages
        headings = _get_headings(pages)

    sections = _split_pages(pages, headings)

    ret = {}
    for sect, page in sections.items():
        if sect != "Docket":  # Don't care about the "docket" section
            ret[sect] = parsers[sect](page)

    return ret


def _get_headings(pages: List[Page]) -> List[List[Dict]]:
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


def _split_pages(
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
            bbox = _calc_bbox(page, pair[0], pair[1])
            sects[str.title(pair[0]["text"])] = page.within_bbox(bbox)

        last = pairs[-1][1]
        bbox = (0, last["bottom"], page.width, page.height - BOTTOM_HEIGHT)
        sects[str.title(last["text"])] = page.within_bbox(bbox)

    return sects


def _calc_bbox(page: Page, h1: Dict, h2: Dict) -> Tuple:
    """Gets bounding box between two headings.

    Args:
        page: PDF page
        h1: First heading. Must be above `h2`
        h2: Second heading

    Returns:
        Tuple: Bounding box (left, top, right, bottom)
    """
    return (0, h1["bottom"], page.width, h2["top"])


def _join_words(w1: Dict, w2: Dict) -> Dict:
    """Join two word dicts.

    Join the text of two words and correct x dimensions

    Args:
        w1: Left word
        w2: Right word

    Returns:
        Dict: Joined word
    """
    temp = w1
    temp["text"] = w1["text"] + " " + w2["text"]
    temp["x0"] = w1["x0"]
    temp["x1"] = w2["x1"]

    return temp


def _get_columns(words: List, headers: List[str]) -> List:
    """Finds columns based on headers.

    Finds column members by finding all words in `words` that are below `head`
    and have (roughly) the same x0 value as `header[i]` for all headers in
    `headers`. Pads lists with "{"text": ""} which is the pdfplumber equivalent
    of an empty string.

    Args:
        words: List of word objects
        headers: List of column headers

    Returns:
        List: Cells of the column
    """
    cols = []
    for header in headers:
        head = next((w for w in words if w["text"] == header))
        rows = []
        for word in words:
            left_aligned = abs(word["x0"] - head["x0"]) < 0.5
            right_aligned = abs(word["x1"] - head["x1"]) < 0.5
            below_header = word["bottom"] >= head["bottom"]

            if (left_aligned or right_aligned) and below_header:
                rows.append(word)

        cols.append(rows)

    num_rows = max(len(x) for x in cols)
    for col in cols:
        col += [{"text": ""}] * (num_rows - len(col))

    return cols


def _columns_to_items_list(cols: List, headers: List[str]) -> List[Dict]:
    rows = [list(a) for a in zip(*cols)]
    ret = []
    for row in rows[1:]:  # First row is the headers
        ret.append({k: v["text"] for k, v in zip(headers, row)})
    return ret


def _split_page_by_x(page: Page, splits: Union[float, List[float]]) -> List:
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


def _parse_col_with_headers_sect(page: Page, headers: List[str]) -> Dict:
    """Parse a section that is columnar with potential key-value pairs.

    Takes a section and list of headers, then searches for those headers in the
    page. Every word that shares an x0 (left side) is considered a column
    member. These rows are turned into a list of dicts called "Items". The rest
    of the words are then treated as key-value pairs. The final Dict will be of
    the form:
    {
        "Key": "Value",
        "Key": "Value",
        ...
        "Items": [
            {<row>},
            {<row>},
            ...
        ]
    }


    Args:
        page: PDF Page. Should be the cropped section of interest.
        headers: List of column headers. Everything else will be parsed as
            key-value pairs

    Returns:
        Dict: Parsed section with key-value pairs and a list of Dicts "items"
    """
    words = page.extract_words(keep_blank_chars=True)
    ret: Dict = {}

    cols = _get_columns(words, headers)
    ret["Items"] = _columns_to_items_list(cols, headers)

    unused = [w for w in words if w not in chain(*cols)]
    unused = list(sorted(unused, key=lambda w: (w["bottom"], w["x0"])))

    # Key-value pairs can potentially be separeted and not joined during
    # extract_words. It's easiest to attempt to join them then parse with regex.
    sep = 20
    pairs = utils.pairwise(unused.copy())
    for w1, w2 in pairs:
        if (w2['x0'] - w1['x1'] < sep) and (abs(w1["bottom"] - w2["bottom"]) < 0.5):
            unused.remove(w1)
            unused.remove(w2)
            unused.append(_join_words(w1, w2))
            try:
                next(pairs)
            except StopIteration:
                pass

    pat = re.compile(r"([\w\s]+):\s*(.*)?")
    still_unused = []
    for w in unused:
        match = pat.match(w['text'])
        if match is None:
            still_unused.append(w)
            continue

        if match.group(2):
            ret[match.group(1)] = match.group(2)
        else:
            ret[match.group(1)] = ""

    still_unused_iter = iter(still_unused)
    for w in still_unused_iter:
        ret[w["text"].replace(":", "")] = next(still_unused_iter)["text"]

    return ret


def _parse_case_info(page: Page, pad: float = 10.0) -> Dict:
    # FIXME: Breaks if >2 things on one line (e.g. OTN/LOTN)
    # FIXME: Breaks if line wraps
    # FIXME: Breaks on CP Criminal Docket (Case Local info)
    texts = []
    pat = re.compile(r"([\s\S]+):\s?(.*)")
    splits = _split_page_by_x(page, page.width // 2 - pad)
    texts += splits[0].extract_text(keep_blank_chars=True).splitlines()
    texts += splits[1].extract_text(keep_blank_chars=True).splitlines()

    ret = {}
    for text in texts:
        search = re.search(pat, text)
        if search is None:
            continue

        ret[search.group(1).strip()] = search.group(2).strip()

    return ret


def _parse_status_info(page: Page) -> Dict:
    headers = ["Status Date", "Processing Status"]
    return _parse_col_with_headers_sect(page, headers)


def _parse_cal_events(page: Page) -> Dict:
    return {}


def _parse_defendant_info(page: Page) -> Dict:
    return {}


def _parse_case_participants(page: Page) -> Dict:
    return {}


def _parse_bail(page: Page) -> Dict:
    headers = [
        "Bail Action Type",
        "Bail Action Date",
        "Bail Type",
        "Percentage",
        "Amount",
    ]
    return _parse_col_with_headers_sect(page, headers)


def _parse_charges(page: Page) -> Dict:
    return {}


def _parse_docket_entry_info(page: Page) -> Dict:
    return {}
