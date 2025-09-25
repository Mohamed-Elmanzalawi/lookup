from lookup import get_citations_by_id, get_name_by_orcid, get_info_by_name
import pytest


def test_get_citations_by_id():
    scopus_id = "8390810700"
    citations = get_citations_by_id(scopus_id)
    assert citations >= 30256


def test_get_name_by_orcid():
    orcid_id = "0000-0002-6782-5715"
    first_name, last_name = get_name_by_orcid(orcid_id)
    assert first_name == "Yasukazu"
    assert last_name == "Nakamura"


def test_get_info_by_name():
    wrong_first_name = "Yasukazu_X"
    last_name = "Nakamura"
    with pytest.raises(SystemExit) as e:
        get_info_by_name(last_name, wrong_first_name)
    assert e.value.code == 0
