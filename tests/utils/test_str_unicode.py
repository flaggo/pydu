# coding: utf-8
from pydu.utils import safestr, safeunicode


def test_safestr():
    assert safestr('hello') == 'hello'
    assert safestr(1) == '1'
    assert list(safestr([1, 'a'])) == ['1', 'a']
    assert safestr(u'中文') == '中文'


def test_safeunicode():
    assert safeunicode('hello') == u'hello'
    assert safeunicode(1) == u'1'
    assert safeunicode('中文') == u'中文'
