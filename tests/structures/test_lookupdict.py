import pytest
from pylib.structures import LookupDict


@pytest.fixture(scope='function')
def lookup_dict():
    d = LookupDict()
    return d


def test_key_exist(lookup_dict):
    lookup_dict['key'] = 1
    assert lookup_dict['key'] == 1


def test_key_not_exist(lookup_dict):
    assert lookup_dict['key'] is None
