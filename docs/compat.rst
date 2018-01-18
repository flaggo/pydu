Compat
------

.. py:data:: pydu.compat.PY2

    Specify current Python interpreter is Python 2 or 3.


.. py:function:: pydu.compat.urlib(base, url, allow_fragments=True)

    Same to ``urllib`` on PY2 or ``urllib.request`` on PY3.


.. py:function:: pydu.compat.urlparse(base, url, allow_fragments=True)

    Same to ``urlparse`` on PY2 or ``urllib.parse`` on PY3.


.. py:function:: pydu.compat.urljoin(base, url, allow_fragments=True)

    Same to ``urlparse.urljoin`` on PY2 or ``urllib.parse.urljoin`` on PY3.


.. py:function:: pydu.compat.iterkeys(d)

    Return an iter object of dictionary keys.


.. py:function:: pydu.compat.itervalues(d)

    Return an iter object of dictionary values.


.. py:function:: pydu.compat.iteritems(d)

    Return an iter object of dictionary items.


.. py:data:: pydu.compat.text_type

    The text type is ``unicode`` on PY2 or ``str`` on PY3.


.. py:data:: pydu.compat.string_types

    The string types are ``(str, unicode)`` on PY2 or ``(str,)`` on PY3.

.. py:data:: pydu.compat.strbytes_types

    The string types are ``(str, unicode, bytes)`` on PY2 or ``(str, bytes)`` on PY3.


.. py:data:: pydu.compat.numeric_types

    The numeric types are ``(int, long)`` on PY2 or ``(int,)`` on PY3.


.. py:function:: pydu.compat.imap(function, sequence, *sequence_1)

    Same to ``itertools.imap`` on PY2 or ``map`` on PY3.


.. py:function:: pydu.compat.cmp(x, y)

    Same to ``cmp`` on PY2, but implement on PY3.


.. py:function:: pydu.compat.has_next_attr(x)

    An implementation independent way of checking for next attribute.


.. py:function:: pydu.compat.is_iterable(x)

    An implementation independent way of checking for iterables.

    >>> from pydu.compat import is_iterable
    >>> is_iterable([])
    True
    >>> is_iterable(1)
    False
