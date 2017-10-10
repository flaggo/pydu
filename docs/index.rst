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




    >>> from pydu.structures import LookupDict
    >>> d = LookupDict()
    >>> d['key']
    None
    >>> d['key'] = 1
    >>> d['key']
    1




  >>> from pydu.structures import LookupDict
  >>> d = LookupDict()
  >>> d['key']
  None
  >>> d['key'] = 1
  >>> d['key']
  1


Utils
=====
