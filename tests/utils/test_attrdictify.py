from pydu.structures import AttrDict
from pydu.utils import attrdictify


def test_attrdictify():
    assert attrdictify({'a': [1, 2]}).a == 2
    assert attrdictify({'a': [1, 2]}, a=[]).a == [1, 2]
    assert attrdictify({'a': 1}, a=[]).a == [1]
    assert attrdictify({}, a=[]).a == []
    assert attrdictify({'a': AttrDict(value=1)}).a == 1
    assert attrdictify({'a': AttrDict(value=1)}, a={}).a == AttrDict(value=1)
    assert attrdictify({}, a={}).a == {}
