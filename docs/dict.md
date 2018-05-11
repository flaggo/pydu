# Dict

Additional powerful dictionaries and relative functions.

## dict.AttrDict
```python
AttrDict(seq=None, **kwargs)
```

A AttrDict object is like a dictionary except `obj.foo` can be used
in addition to `obj['foo']`.

```python
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
```


## dict.CaseInsensitiveDict
```python
CaseInsensitiveDict(data=None, **kwargs)
```

A case-insensitive `dict`-like object.
Implements all methods and operations of `collections.MutableMapping`
as well as dict's `copy`. Also provides `lower_items`.
All keys are expected to be strings. The structure remembers the
case of the last key to be set, and `iter(instance)`, `keys()`,
`items()`, `iterkeys()`, and `iteritems()` will contain
case-sensitive keys.

```python
>>> from pydu.dict import CaseInsensitiveDict
>>> cid = CaseInsensitiveDict()
>>> cid['Accept'] = 'application/json'
>>> cid['aCCEPT'] == 'application/json'
True
>>> list(cid) == ['Accept']
True
```


## dict.LookupDict
```python
LookupDict(name=None)
```

Dictionary lookup object.

```python
>>> from pydu.dict import LookupDict
>>> d = LookupDict()
>>> d['key']
None
>>> d['key'] = 1
>>> d['key']
1
```

## dict.OrderedDefaultDict
```python
OrderedDefaultDict(default_factory=None, *args, **kwds)
```

Dictionary that remembers insertion order and has default value
with default factory.

The default factory is called without arguments to produce
a new value when a key is not present, in `__getitem__` only.
An `OrderedDefaultDict` compares equal to a `collections.defaultdict`
with the same items. All remaining arguments are treated the same
as if they were passed to the `defaultdict` constructor,
including keyword arguments.

```python
>>> from pydu.dict import OrderedDefaultDict
>>> d = OrderedDefaultDict(int)
>>> d['b']
0
>>> d['a']
0
>>> d.keys()
odict_keys(['b', 'a'])
```


## dict.attrify
```python
attrify(obj)
```

Attrify obj into `AttriDict` or `list of AttriDict` if the obj is list.
If obj or the item of obj is not list or dict, will return itself.

```python
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
```
