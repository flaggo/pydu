# coding: utf-8
from pydu.compat import PY2, text_type, imap, has_next_attr


def safeunicode(obj, encoding='utf-8'):
    r"""
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
    elif t is text_type:
        return t
    else:
        return text_type(obj)


def safestr(obj, encoding='utf-8'):
    r"""
    Converts any given object to utf-8 encoded string.

        >>> safestr('hello')
        'hello'
        >>> safestr(2)
        '2'
    """

    if PY2 and isinstance(obj, unicode):
        return obj.encode(encoding)
    elif has_next_attr(obj) or isinstance(obj, iters):
        return imap(safestr, obj)
    else:
        return str(obj)


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
