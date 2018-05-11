# Dict

增强的字典和相关函数。

## dict.AttrDict
```python
AttrDict(seq=None, **kwargs)
```

AttrDict 对象类似于字典，除了能使用 `obj['foo']`，还能使用 `obj.foo`。

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

大小写不敏感类 `字典` 对象。实现了 `collections.MutableMapping` 的所有方法和操作，
也实现了字典的 `copy`，此外还提供 `lower_items`。所有的键都应是字符串。
内部结构会记住最后一次被设置的键的大小写，`iter(instance)`、`keys()`、`items()`、
`iterkeys()` 和 `iteritems()` 将会包含大小写敏感的键。

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

字典查找对象。

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

记住插入顺序且能根据默认工厂提供默认值的字典。

当key不存在（仅限通过 `__getitem__` 中）时，无参数调用默认工厂来产生新值。
`OrderedDefaultDict` 和 `collections.defaultdict` 在比较时是等同的。
所有剩余参数和传入 `defaultdict` 构造器中的相同，包括关键字参数。

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

将对象属性化为 `AttriDict` 或 包含 `AttriDict` 的列表（如果对象为列表）。
如果对象或对象中的元素不是列表或字典，将会返回其本身。

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
