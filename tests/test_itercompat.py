from pydu.itercompat import is_iterable


def test_is_iterable():
    assert is_iterable(list())
    assert is_iterable(tuple())
    assert is_iterable(dict())
    assert is_iterable(set())
    assert not is_iterable(1)
