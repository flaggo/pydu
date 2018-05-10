# compat

compatible data structures, libs, functions for Python 2 and 3.

## compat.PY2

Specify current Python interpreter is Python 2 or 3.


## compat.urlib
```python
urlib(base, url, allow_fragments=True)
```

Same to ``urllib`` on PY2 or ``urllib.request`` on PY3.


## compat.urlparse
```python
urlparse(base, url, allow_fragments=True)
```

Same to ``urlparse`` on PY2 or ``urllib.parse`` on PY3.


## compat.urljoin
```python
urljoin(base, url, allow_fragments=True)
```

Same to ``urlparse.urljoin`` on PY2 or ``urllib.parse.urljoin`` on PY3.


## compat.iterkeys
```python
iterkeys(d)
```

Return an iter object of dictionary keys.


## compat.itervalues
```python
itervalues(d)
```

Return an iter object of dictionary values.


## compat.iteritems
```python
iteritems(d)
```

Return an iter object of dictionary items.


## compat.text_type

The text type is ``unicode`` on PY2 or ``str`` on PY3.


## compat.string_types

The string types are ``(str, unicode)`` on PY2 or ``(str,)`` on PY3.

## compat.strbytes_types

The strbytes(string bytes) types are ``(str, unicode, bytes)`` on PY2 or ``(str, bytes)`` on PY3.


## compat.numeric_types

The numeric types are ``(int, long)`` on PY2 or ``(int,)`` on PY3.


## compat.imap
```python
imap(func, *iterables)
```

Same to ``itertools.imap`` on PY2 or ``map`` on PY3.


## compat.izip
```python
izip(iter1 [,iter2 [...])
```

Same to ``itertools.izip`` on PY2 or ``zip`` on PY3.


## compat.reduce
```python
reduce(function, sequence, initial=None)
```

Same to built-in ``reduce`` on PY2 or ``functools.reduce`` on PY3.


## compat.cmp
```python
cmp(x, y)
```

Same to ``cmp`` on PY2, but implement on PY3.


## compat.has_next_attr
```python
has_next_attr(x)
```

An implementation independent way of checking for next attribute.


## compat.is_iterable
```python
is_iterable(x)
```

An implementation independent way of checking for iterables.

```python
>>> from pydu.compat import is_iterable
>>> is_iterable([])
True
>>> is_iterable(1)
False
```
