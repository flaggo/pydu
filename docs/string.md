# String

Utils for handling string.

## string.safeunicode
```python
safeunicode(obj, encoding='utf-8')
```

Converts any given object to unicode string.

```python
>>> from pydu.string import safeunicode
>>> safeunicode('hello')
u'hello'
>>> safeunicode(2)
u'2'
>>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
u'中文'
```


## string.safeencode
```python
safeencode(obj, encoding='utf-8')
```

Converts any given object to encoded string (default: utf-8).

```python
>>> from pydu.string import safeencode
>>> safeencode('hello')
'hello'
>>> safeencode(2)
'2'
>>> safeencode(u'中文')
'\xe4\xb8\xad\xe6\x96\x87'
```


## string.lstrips
```python
lstrips(text, remove)
```

Removes the string `remove` from the left of `text`.

```python
>>> from pydu.string import lstrips
>>> lstrips('foobar', 'foo')
'bar'
>>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
'BAZ'
>>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
'BARBAZ'
```


## string.rstrips
```python
rstrips(text, remove)
```

Removes the string `remove` from the right of `text`.

```python
>>> from pydu.string import rstrips
>>> rstrips('foobar', 'bar')
'foo'
```


## string.strips
```python
strips(text, remove)
```

Removes the string `remove` from the both sides of `text`.

```python
>>> from pydu.string import strips
>>> strips('foobarfoo', 'foo')
'bar'
```

## string.common_prefix
```python
common_prefix(l)
```

Return common prefix of the stings

```python
>>> from pydu.string import common_prefix
>>> common_prefix(['abcd', 'abc1'])
'abc'
```


## string.common_suffix
```python
common_suffix(l)
```

Return common suffix of the stings

```python
>>> from pydu.string import common_suffix
>>> common_suffix(['dabc', '1abc'])
'abc'
```


## string.sort
```python
sort(s, reversed=False)
```

Sort given string by ascending order.
If `reverse` is `True`, sorting given string by descending order.

```python
>>> from pydu.string import sort
>>> sort('dabc')
'abcd'
```
