# coding: utf-8
import collections

from .compat import PY2


class AttrDict(dict):
    """
    A AttrDict object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.

        >>> o = AttrDict(a=1)
        >>> o.a
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

    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<AttrDict ' + dict.__repr__(self) + '>'


class CaseInsensitiveDict(collections.MutableMapping):
    """
    A case-insensitive ``dict``-like object.
    Implements all methods and operations of
    ``collections.MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.
    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive:
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.
    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    """
    def __init__(self, data=None, **kwargs):
        self._store = {}
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return (
            (lowerkey, keyval[1])
            for (lowerkey, keyval)
            in self._store.items()
        )

    def __eq__(self, other):
        if isinstance(other, collections.Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
         return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, dict(self.items()))


class LookupDict(dict):
    """
    Dictionary lookup object.
        d = LookupDict()
        print(d['key'])  # None
        d['key'] = 1
        print(d['key'])  # 1
    """

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None
        return self.get(key, None)


# https://stackoverflow.com/questions/6190331/can-i-do-an-ordered-default-dict-in-python
class OrderedDefaultDict(collections.OrderedDict):
    """
    Dictionary that remembers insertion order and has default value
    with default factory.

    The default factory is called without arguments to produce
    a new value when a key is not present, in `__getitem__` only.
    An `OrderedDefaultDict` compares equal to a `collections.defaultdict`
    with the same items. All remaining arguments are treated the same
    as if they were passed to the `defaultdict` constructor,
    including keyword arguments.
    """
    def __init__(self, default_factory=None, *args, **kwds):
        if (default_factory is not None and
           not isinstance(default_factory, collections.Callable)):
            raise TypeError('First argument must be callable')
        super(OrderedDefaultDict, self).__init__(*args, **kwds)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return super(OrderedDefaultDict, self).__getitem__(key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return self.__class__(self.default_factory, self)

    if PY2:
        def __deepcopy__(self, memo):
            import copy
            return self.__class__(self.default_factory, copy.deepcopy(self.items()))
    else:
        def __deepcopy__(self, memo):
            import copy
            return self.__class__(self.default_factory, copy.deepcopy(iter(self.items())))

    def __repr__(self):
        return 'OrderedDefaultDict({default_factory}, {repr})'.format(
            default_factory=self.default_factory,
            repr=super(OrderedDefaultDict, self).__repr__()
        )


def attrify(obj):
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            obj[i] = attrify(v)
        return obj
    elif isinstance(obj, dict):
        attrd = AttrDict()
        for key, value in obj.items():
            value = attrify(value)
            setattr(attrd, key, value)
        return attrd
    else:
        return obj
