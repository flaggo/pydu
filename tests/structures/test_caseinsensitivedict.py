import pytest
from pylib.structures import CaseInsensitiveDict


@pytest.fixture(scope='function')
def case_insensitive_dict():
    d = CaseInsensitiveDict()
    return d


def test_case_insensitive_dict(case_insensitive_dict):
    case_insensitive_dict['Accept'] = 1
    assert case_insensitive_dict['aCCept'] == 1
    assert list(case_insensitive_dict) == ['Accept']
