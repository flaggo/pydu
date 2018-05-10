# compat

提供Python 2和3兼容的数据结构、库和函数。

## compat.PY2

判断当前Python解释器是Python 2还是3。


## compat.urlib
```python
urlib(base, url, allow_fragments=True)
```

在PY2中是 ``urllib``，在PY3中是 ``urllib.request``。


## compat.urlparse
```python
urlparse(base, url, allow_fragments=True)
```

在PY2中是 ``urlparse``，在PY3中是 ``urllib.parse``。


## compat.urljoin
```python
urljoin(base, url, allow_fragments=True)
```

在PY2中是 ``urlparse.urljoin``，在PY3中是 ``urllib.parse.urljoin``。


## compat.iterkeys
```python
iterkeys(d)
```

返回字典键的iter对象。


## compat.itervalues
```python
itervalues(d)
```

返回字典值的iter对象。


## compat.iteritems
```python
iteritems(d)
```

返回字典键值对的iter对象。


## compat.text_type

text类型在PY2中是 ``unicode``，在PY3中是 ``str``。


## compat.string_types

string类型在PY2中是 ``(str, unicode)``，在PY3中是 ``(str,)``。

## compat.strbytes_types

strbytes（string bytes）类型在PY2中是 ``(str, unicode, bytes)``，在PY3中是 ``(str, "
"bytes)``。


## compat.numeric_types

在PY2中是 ``(int, long)``，在PY3中是 ``(int,)``。


## compat.imap
```python
imap(func, *iterables)
```

在PY2中是 ``itertools.imap``，在PY3中是 ``map``。


## compat.izip
```python
izip(iter1 [,iter2 [...])
```

在PY2中是 ``itertools.izip``，在PY3中是 ``zip``。


## compat.reduce
```python
reduce(function, sequence, initial=None)
```

在PY2中是内建 ``reduce``，在PY3中是 ``functools.reduce``。


## compat.cmp
```python
cmp(x, y)
```

Same to ``cmp`` on PY2, but implement on PY3.
在PY2中是内建 ``cmp``，在PY3中则由pydu实现。


## compat.has_next_attr
```python
has_next_attr(x)
```

查看是否有next属性。


## compat.is_iterable
```python
is_iterable(x)
```

查看是否是可迭代的。

```python
>>> from pydu.compat import is_iterable
>>> is_iterable([])
True
>>> is_iterable(1)
False
```
