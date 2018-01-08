# coding: utf-8
import pytest
from pydu.string import (safeencode, safeunicode, strips, lstrips, rstrips,
                         common_prefix, common_suffix, sort, boolean)


def test_safeencode():
    assert safeencode('hello') == b'hello'
    assert safeencode(1) == b'1'
    assert safeencode(u'中文') == b'\xe4\xb8\xad\xe6\x96\x87'


def test_safeunicode():
    assert safeunicode('hello') == u'hello'
    assert safeunicode(1) == u'1'
    assert safeunicode('中文') == u'中文'

    assert safeunicode(u'hello') == u'hello'
    assert safeunicode(u'中文') == u'中文'


def test_lstrips():
    assert lstrips('foobbar', '') == 'foobbar'
    assert lstrips('foobar', 'fo') == 'obar'
    assert lstrips('foofoobar', 'foo') == 'foobar'
    assert lstrips('foobarbaz', ('foo', 'bar')) == 'baz'
    assert lstrips('foobarbaz', ('bar', 'foo')) == 'barbaz'


def test_rstrips():
    assert rstrips('foobbar', '') == 'foobbar'
    assert rstrips('foobbar', 'bar') == 'foob'
    assert rstrips('foobarbar', 'bar') == 'foobar'
    assert rstrips('fozfoobar', ('bar', 'foo')) == 'foz'
    assert rstrips('fozfoobar', ('foo', 'bar')) == 'fozfoo'


def test_strips():
    assert strips('foobarfoo', '') == 'foobarfoo'
    assert strips('foobarfoo', 'foo') == 'bar'
    assert strips('foobarfoo', ('foo', 'bar')) == ''


def test_common_prefix():
    l = ['abcd', 'abc1']
    assert common_prefix(l) == 'abc'


def test_common_suffix():
    l = ['dabc', '1abc']
    assert common_suffix(l) == 'abc'


def test_sort():
    assert sort('acb21') == '12abc'
    assert sort('abc21', reverse=True) == 'cba21'


class TestBoolean:
    def test_accepted_text(self):
        for text in ('yes', 'y', 'on', 'true', 't', '1'):
            assert boolean(text)
            assert boolean(text.upper())

        for text in ('no', 'n', 'off', 'false', 'f', '0'):
            assert not boolean(text)
            assert not boolean(text.upper())

    @pytest.mark.parametrize('text', ('a', 'b'))
    def test_unaccepted_text(self, text):
        with pytest.raises(ValueError):
            boolean(text)

    def test_nonstring(self):
        for obj in (10, [1], {1: 1}):
            assert boolean(obj)

        for obj in (0, [], {}):
            assert not boolean(obj)
