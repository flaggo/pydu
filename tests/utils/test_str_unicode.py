# coding: utf-8
from pylib.utils import safestr, safeunicode


def test_safestr():
    assert safestr('hello') == 'hello'
    assert safestr(1) == '1'
    assert list(safestr([1, 'a'])) == ['1', 'a']


def test_safeunicode():
    assert safeunicode('hello') == u'hello'
    assert safeunicode(1) == u'1'
    assert safeunicode('中文') == u'中文'
