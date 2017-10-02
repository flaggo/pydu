from .structures import AttrDict
from .py3helpers import PY2, itervalues, iteritems, text_type, string_types, imap, is_iter


def attrdictify(mapping, *requireds, **defaults):
    """
    Creates a `AttrDict` object from dictionary `mapping`, raising `KeyError` if
    d doesn't have all of the keys in `requireds` and using the default
    values for keys found in `defaults`.
    For example, `attrdictify({'a':1, 'c':3}, b=2, c=0)` will return the equivalent of
    `AttrDict({'a':1, 'b':2, 'c':3})`.

    If a `attrdictify` value is a list (e.g. multiple values in a form submission),
    `attrdictify` returns the last element of the list, unless the key appears in
    `defaults` as a list. Thus:

        >>> attrdictify({'a':[1, 2]}).a
        2
        >>> attrdictify({'a':[1, 2]}, a=[]).a
        [1, 2]
        >>> attrdictify({'a':1}, a=[]).a
        [1]
        >>> attrdictify({}, a=[]).a
        []

    Similarly, if the value has a `value` attribute, `attrdictify will return _its_
    value, unless the key appears in `defaults` as a dictionary.

        >>> attrdictify({'a':attrdict(value=1)}).a
        1
        >>> attrdictify({'a':attrdict(value=1)}, a={}).a
        <AttrDict {'value': 1}>
        >>> attrdictify({}, a={}).a
        {}

    """
    _unicode = defaults.pop('_unicode', False)

    # if _unicode is callable object, use it convert a string to unicode.
    to_unicode = safeunicode
    if _unicode is not False and hasattr(_unicode, '__call__'):
        to_unicode = _unicode

    def unicodify(s):
        if _unicode and isinstance(s, str):
            return to_unicode(s)
        else:
            return s

    def getvalue(x):
        if hasattr(x, 'file') and hasattr(x, 'value'):
            return x.value
        elif hasattr(x, 'value'):
            return unicodify(x.value)
        else:
            return unicodify(x)

    attrd = AttrDict()
    for key in requireds + tuple(mapping.keys()):
        value = mapping[key]
        if isinstance(value, list):
            if isinstance(defaults.get(key), list):
                value = [getvalue(x) for x in value]
            else:
                value = value[-1]
        if not isinstance(defaults.get(key), dict):
            value = getvalue(value)
        if isinstance(defaults.get(key), list) and not isinstance(value, list):
            value = [value]

        setattr(attrd, key, value)

    for (key, value) in iteritems(defaults):
        result = value
        if hasattr(attrd, key):
            result = attrd[key]
        if value == () and not isinstance(result, tuple):
            result = (result,)
        setattr(attrd, key, result)

    return attrd


def safeunicode(obj, encoding='utf-8'):
    r"""
    Converts any given object to unicode string.

        >>> safeunicode('hello')
        u'hello'
        >>> safeunicode(2)
        u'2'
        >>> safeunicode('\xe1\x88\xb4')
        u'\u1234'
    """
    t = type(obj)
    if t is text_type:
        return obj
    elif t is bytes:
        return obj.decode(encoding)
    elif t in [int, float, bool]:
        return unicode(obj)
    else:
        return unicode(obj)


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
    elif is_iter(obj):
        return imap(safestr, obj)
    else:
        return str(obj)


if not PY2:
    # Since Python3, utf-8 encoded strings and unicode strings are the same thing
    safeunicode = safestr


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
