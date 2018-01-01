import pytest
import unittest

from pydu.dict import AttrDict, LookupDict, CaseInsensitiveDict, OrderedDefaultDict, attrify


class TestAttrDict:

    def test_attr_access_with_init(self):
        d = AttrDict(key=1)
        assert d['key'] == 1
        assert d.key == 1

    def test_attr_access_without_init(self):
        d = AttrDict()
        d['key'] = 1
        assert d['key'] == 1
        assert d.key == 1

        d.anotherkey = 1
        assert d.anotherkey == 1
        assert d['anotherkey'] == 1

    def test_attr_delete(self):
        d = AttrDict(key=1)
        del d.key
        with pytest.raises(AttributeError):
            del d.key

    def test_repr(self):
        d = AttrDict()
        assert repr(d) == '<AttrDict {}>'


class TestLooUpDict:

    def test_key_exist(self):
        d = LookupDict()
        d['key'] = 1
        assert d['key'] == 1

    def test_key_not_exist(self):
        d = LookupDict()
        assert d['key'] is None


class TestCaseInsensitiveDict(unittest.TestCase):
    def setUp(self):
        self.d = CaseInsensitiveDict()
        self.d['Accept'] = 1

    def test_ci_dict_set(self):
        assert self.d['aCCept'] == 1
        assert list(self.d) == ['Accept']

    def test_ci_dict_del(self):
        del self.d['accept']
        assert not self.d

    def test_ci_dict_copy_and_equal(self):
        d = self.d.copy()
        assert d == self.d


class TestOrderedDefaultDict:
    def test_default_normal(self):
        d = OrderedDefaultDict(int)
        assert d[1] == 0
        assert d['a'] == 0
        d[2] = 2
        assert d[2] == 2
        assert list(d.keys()) == [1, 'a', 2]

        d = OrderedDefaultDict(int, a=1)
        assert d['a'] == 1

    def test_default_factory_not_callable(self):
        with pytest.raises(TypeError):
            OrderedDefaultDict('notcallable')

    def test_default_factory_none(self):
        d = OrderedDefaultDict()
        with pytest.raises(KeyError):
            d[1]

    def test_copy(self):
        d1 = OrderedDefaultDict(int, a=[])
        d2 = d1.copy()
        assert d2['a'] == []
        d1['a'].append(1)
        assert d2['a'] == [1]

    def test_deepcopy(self):
        import copy
        d1 = OrderedDefaultDict(int, a=[])
        d2 = copy.deepcopy(d1)
        assert d2['a'] == []
        d1['a'].append(1)
        assert d2['a'] == []

    def test_repr(self):
        d = OrderedDefaultDict(int, a=1)
        assert repr(d).startswith('OrderedDefaultDict')

def test_attrify():
    attrd = attrify({
        'a': [1, 2, {'b': 'b'}],
        'c': 'c',
    })
    assert attrd.a == [1, 2, {'b': 'b'}]
    assert attrd.a[2].b == 'b'
    assert attrd.c == 'c'

    attrd = attrify((1, 2))
    assert attrd == (1, 2)

    attrd = attrify({
        'a': 1,
        'b': (1, 2)
    })
    assert attrd.a == 1
    assert attrd.b == (1, 2)
