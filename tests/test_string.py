# coding: utf-8
from pydu.string import safeencode, safeunicode, strips, lstrips, rstrips


def test_safeencode():
    assert safeencode('hello') == 'hello'
    assert safeencode(1) == '1'
    assert safeencode(u'中文') == '中文'


def test_safeunicode():
    assert safeunicode('hello') == u'hello'
    assert safeunicode(1) == u'1'
    assert safeunicode('中文') == u'中文'


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
