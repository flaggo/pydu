import pytest
from pylib.structures import AttrDict


def test_attr_access_with_init():
    d = AttrDict(key=1)
    assert d['key'] == 1
    assert d.key == 1


def test_attr_access_without_init():
    d = AttrDict()
    d['key'] = 1
    assert d['key'] == 1
    assert d.key == 1

    d.anotherkey = 1
    assert d.anotherkey == 1
    assert d['anotherkey'] == 1


def test_attr_delete():
    d = AttrDict(key=1)
    del d.key
    with pytest.raises(AttributeError):
        d.key


def test_repr():
    d = AttrDict()
    assert repr(d) == '<AttrDict {}>'
