import pytest
from pydu.iter import first, last


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
