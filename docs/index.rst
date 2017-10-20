.. pydu documentation master file, created by
   sphinx-quickstart on Fri Oct  6 23:05:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pydu documentation
===================

About
-----

**pydu** (python data structures and utils) is a library for Python 2 and 3.
It is collected from open source projects and created by contributors.

It is with Python versions from **2.7 to 3.6**.

The pydu documentation you're reading is distributed as a single HTML page.


Data Structures
===============

Dict
----

.. class:: pydu.structures.AttrDict(seq=None, **kwargs)

  A AttrDict object is like a dictionary except `obj.foo` can be used
  in addition to `obj['foo']`.

    >>> from pydu.structures import AttrDict
    >>> o = AttrDict(a=1)
    o.a
    1
    >>> o['a']
    1
    >>> o.a = 2
    >>> o['a']
    2
    >>> del o.a
    >>> o.a
    Traceback (most recent call last):
        ...
    AttributeError: 'a'


.. class:: pydu.structures.CaseInsensitiveDict(data=None, **kwargs)

  A case-insensitive ``dict``-like object.
  Implements all methods and operations of ``collections.MutableMapping``
  as well as dict's ``copy``. Also provides ``lower_items``.
  All keys are expected to be strings. The structure remembers the
  case of the last key to be set, and ``iter(instance)``, ``keys()``,
  ``items()``, ``iterkeys()``, and ``iteritems()`` will contain
  case-sensitive keys.

    >>> from pydu.structures import CaseInsensitiveDict
    >>> cid = CaseInsensitiveDict()
    >>> cid['Accept'] = 'application/json'
    >>> cid['aCCEPT'] == 'application/json'
    True
    >>> list(cid) == ['Accept']
    True

  case-sensitive keys.

    >>> from pydu.structures import CaseInsensitiveDict
    >>> cid = CaseInsensitiveDict()
    >>> cid['Accept'] = 'application/json'
    >>> cid['aCCEPT'] == 'application/json'
    True
    >>> list(cid) == ['Accept']
    True


.. class:: pydu.structures.LookupDict(name=None)

  Dictionary lookup object.

    >>> from pydu.structures import LookupDict
    >>> d = LookupDict()
    >>> d['key']
    None
    >>> d['key'] = 1
    >>> d['key']
    1


Set
----

.. class:: pydu.structures.OrderedSet(iterable=None)

  A set which keeps the ordering of the inserted items.

    >>> from pydu.structures import OrderedSet
    >>> s = OrderedSet([1, 3, 1, 2])
    >>> list(s)
    [1, 3, 2]
    >>> s.discard(3)
    >>> list(s)
    [1, 2]


Utils
=====

Dict
----

.. function:: pydu.utils.attrify(obj)

  Attrify obj into `AttriDict` or list or `AttriDict` if the obj is list.

    >>> from pydu.utils import attrify
    >>> attrd = attrify({
        'a': [1, 2, {'b': 'b'}],
        'c': 'c',
    })
    >>> attrd
    <AttrDict {'a': [1, 2, <AttrDict {'b': 'b'}>], 'c': 'c'}>
    >>> attrd.a
    1
    >>> attrd.a[2].b
    b
    >>> attrd.c
    c


String
------

.. function:: pydu.utils.safeunicode(obj, encoding='utf-8')

  Converts any given object to unicode string.

    >>> safeunicode('hello')
    u'hello'
    >>> safeunicode(2)
    u'2'
    >>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
    u'中文'


.. function:: pydu.utils.safestr(obj, encoding='utf-8')

  Converts any given object to utf-8 encoded string.

    >>> safestr('hello')
    'hello'
    >>> safestr(2)
    '2'
    >>> safestr(u'中文')
    '中文'


.. function:: pydu.utils.lstrips(text, remove)

  Removes the string `remove` from the left of `text`.

    >>> lstrips('foobar', 'foo')
    'bar'
    >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
    'BAZ'
    >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
    'BARBAZ'


.. function:: pydu.utils.rstrips(text, remove)

  Removes the string `remove` from the right of `text`.

    >>> rstrips('foobar', 'bar')
    'foo'


.. function:: pydu.utils.strips(text, remove)

  Removes the string `remove` from the both sides of `text`.

    >>> strips('foobarfoo', 'foo')
    'bar'
