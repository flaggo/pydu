import pytest
import unittest
from pydu.datastructures.dict import AttrDict, LookupDict, CaseInsensitiveDict


class TestAttrDict(object):

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
            d.key

    def test_repr(self):
        d = AttrDict()
        assert repr(d) == '<AttrDict {}>'


class TestLooUpDict(object):

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
