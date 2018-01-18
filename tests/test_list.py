import pytest
from pydu.list import uniq, tolist


def test_uniq():
    assert uniq([1, 4, 0, 2, 0, 3]) == [1, 4, 0, 2, 3]


@pytest.mark.parametrize('obj', ('foo', ['foo']))
def test_tolist(obj):
    assert tolist(obj) == ['foo']
