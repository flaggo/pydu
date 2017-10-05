import pytest
from pylib.structures import CaseInsensitiveDict


@pytest.fixture(scope='function')
def ci_dict():
    d = CaseInsensitiveDict()
    d['Accept'] = 1
    return d


def test_ci_dict_set(ci_dict):
    assert ci_dict['aCCept'] == 1
    assert list(ci_dict) == ['Accept']


def test_ci_dict_del(ci_dict):
    del ci_dict['accept']
    assert not ci_dict


def test_ci_dict_copy_and_equal(ci_dict):
    d = ci_dict.copy()
    assert d == ci_dict
