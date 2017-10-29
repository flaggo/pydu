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


Content
===============

Archive
-------

.. function:: pydu.archive.extract(path, to_path='', ext='')

  Unpack the tar or zip file at the specified path or file to the directory
  specified by ``to_path``. It supports many extensions, like ``.tar``,
  ``.tar.bz2``, ``.tar.gz``, ``.tgz``, ``.tz2``, ``.zip``. If the file name of
  given ``path`` doesn't contain file extension, the ``ext`` parameter can be
  specified one of supported extensions to indicate file type.

    >>> from pydu.archive import extract
    >>> extract('foobar.tgz', '/tmp')
    >>> extract('foobar', '/tmp', ext='.tgz')
    >>> extract('foobar', '/tmp')
    Traceback (most recent call last):
     ...    AttributeError: pydu.archive.UnrecognizedArchiveFormat: Path not a recognized archive format: foobar


Dict
----

.. class:: pydu.dict.AttrDict(seq=None, **kwargs)

  A AttrDict object is like a dictionary except ``obj.foo`` can be used
  in addition to ``obj['foo']``.

    >>> from pydu.dict import AttrDict
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
     ...    AttributeError: 'a'


.. class:: pydu.dict.CaseInsensitiveDict(data=None, **kwargs)

  A case-insensitive ``dict``-like object.
  Implements all methods and operations of ``collections.MutableMapping``
  as well as dict's ``copy``. Also provides ``lower_items``.
  All keys are expected to be strings. The structure remembers the
  case of the last key to be set, and ``iter(instance)``, ``keys()``,
  ``items()``, ``iterkeys()``, and ``iteritems()`` will contain
  case-sensitive keys.

    >>> from pydu.dict import CaseInsensitiveDict
    >>> cid = CaseInsensitiveDict()
    >>> cid['Accept'] = 'application/json'
    >>> cid['aCCEPT'] == 'application/json'
    True
    >>> list(cid) == ['Accept']
    True


.. class:: pydu.dict.LookupDict(name=None)

  Dictionary lookup object.

    >>> from pydu.dict import LookupDict
    >>> d = LookupDict()
    >>> d['key']
    None
    >>> d['key'] = 1
    >>> d['key']
    1


.. function:: pydu.dict.attrify(obj)

  Attrify obj into ``AttriDict`` or ``list of AttriDict`` if the obj is list.

    >>> from pydu.dict import attrify
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


Set
----

.. class:: pydu.set.OrderedSet(iterable=None)

  A set which keeps the ordering of the inserted items.

    >>> from pydu.set import OrderedSet
    >>> s = OrderedSet([1, 3, 1, 2])
    >>> list(s)
    [1, 3, 2]
    >>> s.discard(3)
    >>> list(s)
    [1, 2]


String
------

.. function:: pydu.string.safeunicode(obj, encoding='utf-8')

  Converts any given object to unicode string.

    >>> from pydu.string import safeunicode
    >>> safeunicode('hello')
    u'hello'
    >>> safeunicode(2)
    u'2'
    >>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
    u'中文'


.. function:: pydu.string.lstrips(text, remove)

  Removes the string ``remove`` from the left of ``text``.

    >>> from pydu.string import lstrips
    >>> lstrips('foobar', 'foo')
    'bar'
    >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
    'BAZ'
    >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
    'BARBAZ'


.. function:: pydu.string.rstrips(text, remove)

  Removes the string ``remove`` from the right of ``text``.

    >>> from pydu.string import rstrips
    >>> rstrips('foobar', 'bar')
    'foo'


.. function:: pydu.string.strips(text, remove)

  Removes the string ``remove`` from the both sides of ``text``.

    >>> from pydu.string import strips
    >>> strips('foobarfoo', 'foo')
    'bar'


Miscellanea
-----------

.. function:: pydu.unix_timeout(seconds)

  This func decorates any func which may be hang for a while. The param ``seconds``
  should be integer. ``unix_timeout`` can only be used on ``unix-like`` system.
  In `test.py`, you may write like below:

  .. code-block:: python

    import time
    from pydu.utils import unix_timeout
    @unix_timeout(1)
    def f():
        time.sleep(1.01)
    f()

  Ant run `test.py`, will see ``TimeoutError``.


.. function:: pydu.trace(obj)

  Tracing every statement and line number for running program, like ``bash -x``.
  In `test.py`, you may write like below:

  .. code-block:: python

    from pydu import trace
    @trace
    def f():
        print(1)
        a = 1 + 5
        b = [a]
        print(2)
    f()

  Ant run `test.py`, will see below output from console:

  .. code-block:: console

    test.py(4):     print(1)
    1
    test.py(5):     a = 1 + 5
    test.py(6):     b = [a]
    test.py(7):     print(2)
    2
