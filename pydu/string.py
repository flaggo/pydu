# coding: utf-8
import locale
from .compat import text_type


preferredencoding = locale.getpreferredencoding()


def safeunicode(obj, encoding='utf-8'):
    """
    Converts any given object to unicode string.

        >>> safeunicode('hello')
        u'hello'
        >>> safeunicode(2)
        u'2'
        >>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
        u'中文'
    """
    t = type(obj)
    if t is text_type:
        return obj
    elif t is bytes:
        return obj.decode(encoding)
    else:
        return text_type(obj)


def safeencode(obj, encoding='utf-8'):
    """
    Converts any given object to encoded string (default: utf-8).

        >>> safestr('hello')
        'hello'
        >>> safestr(2)
        '2'
    """
    t = type(obj)
    if t is text_type:
        return obj.encode(encoding)
    elif t is bytes:
        return obj
    else:
        return text_type(obj).encode(encoding)


iters = [list, tuple, set, frozenset]
class _hack(tuple): pass
iters = _hack(iters)
iters.__doc__ = """
A list of iterable items (like lists, but not strings). Includes whichever
of lists, tuples, sets, and Sets are available in this version of Python.
"""


def _strips(direction, text, remove):
    if isinstance(remove, iters):
        for subr in remove:
            text = _strips(direction, text, subr)
        return text

    if direction == 'l':
        if text.startswith(remove):
            return text[len(remove):]
    elif direction == 'r':
        if text.endswith(remove):
            return text[:-len(remove) or None]
    else:
        raise ValueError('Direction needs to be r or l.')
    return text


def rstrips(text, remove):
    """
    removes the string `remove` from the right of `text`
        >>> rstrips('foobar', 'bar')
        'foo'
    """
    return _strips('r', text, remove)


def lstrips(text, remove):
    """
    removes the string `remove` from the left of `text`

        >>> lstrips('foobar', 'foo')
        'bar'
        >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
        'BAZ'
        >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
        'BARBAZ'

    """
    return _strips('l', text, remove)


def strips(text, remove):
    """
    removes the string `remove` from the both sides of `text`
        >>> strips('foobarfoo', 'foo')
        'bar'
    """
    return rstrips(lstrips(text, remove), remove)


def common_prefix(l):
    """
    Return common prefix of the stings
        >>> common_prefix(['abcd', 'abc1'])
        'abc'
    """
    commons = []
    for i in range(min(len(s) for s in l)):
        common = l[0][i]
        for c in l[1:]:
            if c[i] != common:
                return ''.join(commons)
        commons.append(common)
    return ''.join(commons)


def common_suffix(l):
    """
    Return common suffix of the stings
        >>> common_suffix(['dabc', '1abc'])
        'abc'
    """
    commons = []
    for i in range(min(len(s) for s in l)):
        common = l[0][-i-1]
        for c in l[1:]:
            if c[-i-1] != common:
                return ''.join(reversed(commons))
        commons.append(common)
    return ''.join(reversed(commons))


def sort(s, reverse=False):
    """
    Sort given string by ascending order.
    If reverse is True, sorting given string by descending order.
    """
    return ''.join(sorted(s, reverse=reverse))
