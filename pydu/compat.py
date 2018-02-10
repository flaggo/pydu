"""Utilities for make the code run both on Python2 and Python3.
"""
import sys
import types

PY2 = sys.version_info[0] == 2


# builtins
if PY2:
    import __builtin__ as builtins
else:
    import builtins

# url*
if PY2:
    import urllib as urlib
    import urlparse
    from urlparse import urljoin
else:
    import urllib.request as urlib
    import urllib.parse as urlparse
    from urllib.parse import urljoin

# Dictionary iteration
if PY2:
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
else:
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

# string and text types
if PY2:
    text_type = unicode
    string_types = (str, unicode)
    strbytes_types = (str, unicode, bytes)
    numeric_types = (int, long)
else:
    text_type = str
    string_types = (str,)
    strbytes_types = (str, bytes)
    numeric_types = (int,)

# imap
if PY2:
    from itertools import imap
else:
    imap = map

if PY2:
    reduce = reduce
else:
    from functools import reduce

# next
if PY2:
    has_next_attr = lambda x: x and hasattr(x, 'next')
else:
    has_next_attr = lambda x: x and hasattr(x, '__next__')

# Class Type
if PY2:
    ClassTypes = (type, types.ClassType)
else:
    ClassTypes = (type,)

# cmp
if PY2:
    cmp = cmp
else:
    cmp = lambda x, y: (x > y) - (x < y)


# is iterable
def is_iterable(x):
    """An implementation independent way of checking for iterables."""
    try:
        iter(x)
    except TypeError:
        return False
    else:
        return True
