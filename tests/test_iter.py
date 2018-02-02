import pytest
from pydu.iter import first, last, all, any, join


@pytest.mark.parametrize(
    'iterable', (
        [1, 2],
        (1, 2),
        {1, 2},
        {1: 1, 2: 2},
        iter([1, 2])
    ))
def test_first_last(iterable):
    assert first(iterable) == 1
    assert last(iterable) == 2


def test_all():
    assert all([0, 1, 2], lambda x: x+1)
    assert not all([0, 1, 2], lambda x: x)


def test_any():
    assert any([-1, -1, 0], lambda x: x+1)
    assert not any([-1, -1, -1], lambda x: x + 1)


def test_join():
    assert join(iter([1, '2', 3])) == '123'
    assert join(iter([1, '2', 3]), separator=',') == '1,2,3'
