from pydu.list import uniq


def test_uniq():
    assert uniq([1, 4, 0, 2, 0, 3]) == [1, 4, 0, 2, 3]
