# noqa: D100
from os import path

import pdfplumber
import pytest

from pollydocket import docket

from .data import docket_output

PDFS_PATH = f"{path.dirname(path.abspath(__file__))}/data/"


@pytest.fixture
def sections(request):  # noqa: D103
    with pdfplumber.open(PDFS_PATH + request.param) as pdf:
        pages = pdf.pages
        headings = docket.get_headings(pages)
        return docket.split_pages(pages, headings)


@pytest.mark.parametrize("test_in,expected_out", docket_output.dicts)
def test_parse_pdf(test_in, expected_out):  # noqa: D103
    test_docket = docket.parse_pdf(PDFS_PATH + test_in)
    assert test_docket == expected_out


@pytest.mark.parametrize("test_in,expected_out", docket_output.headings)
def test_get_headings(test_in, expected_out):  # noqa: D103
    with pdfplumber.open(PDFS_PATH + test_in) as pdf:
        headings = docket.get_headings(pdf.pages)
        test_result = []
        for page in headings:
            test_result.append([h["text"] for h in page])
        assert test_result == expected_out


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_case_info(sections, expected_out):  # noqa: D103
    res = docket.parse_case_info(sections["Case Information"])
    assert res == expected_out["Case Information"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_status_info(sections, expected_out):  # noqa: D103
    if "Status Information" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Status Information"])
        assert res == expected_out["Status Information"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_cal_events(sections, expected_out):  # noqa: D103
    if "Calendar Events" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Calendar Events"])
        assert res == expected_out["Calendar Events"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_defendant_info(sections, expected_out):  # noqa: D103
    if "Defendant Information" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Defendant Information"])
        assert res == expected_out["Defendant Information"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_case_participants(sections, expected_out):  # noqa: D103
    if "Case Participants" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Case Participants"])
        assert res == expected_out["Case Participants"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_bail(sections, expected_out):  # noqa: D103
    if "Bail" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Bail"])
        assert res == expected_out["Bail"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_charges(sections, expected_out):  # noqa: D103
    if "Charges" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Charges"])
        assert res == expected_out["Charges"]


@pytest.mark.parametrize(
    "sections, expected_out", docket_output.dicts, indirect=["sections"]
)
def test_parse_docket_entry_info(sections, expected_out):  # noqa: D103
    if "Docket Entry Information" not in sections:
        assert True
    else:
        res = docket.parse_status_info(sections["Docket Entry Information"])
        assert res == expected_out["Docket Entry Information"]
