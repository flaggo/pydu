import pytest
from pydu.list import uniq, tolist, flatten


def test_uniq():
    assert uniq([1, 4, 0, 2, 0, 3]) == [1, 4, 0, 2, 3]


@pytest.mark.parametrize('obj', ('foo', ['foo']))
def test_tolist(obj):
    assert tolist(obj) == ['foo']


def test_flatten():
    assert list(flatten([1, 2])) == [1, 2]
    assert list(flatten([1, [2, 3]])) == [1, 2, 3]
    assert list(flatten([1, [2, [3, 4]]])) == [1, 2, 3, 4]
