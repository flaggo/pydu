# String

提供处理字符串的工具。

## string.safeunicode
```python
safeunicode(obj, encoding='utf-8')
```

将任何对象转换为 `unicode` 字符串。

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

将任何对象转换为编码后字符串（默认为 `utf-8`）。

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

移除字符串 `text` 左侧的 `remove`。

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

移除字符串 `text` 右侧的 `remove`。

```python
>>> from pydu.string import rstrips
>>> rstrips('foobar', 'bar')
'foo'
```


## string.strips
```python
strips(text, remove)
```

移除字符串 `text` 两边的 `remove`。

```python
>>> from pydu.string import strips
>>> strips('foobarfoo', 'foo')
'bar'
```

## string.common_prefix
```python
common_prefix(l)
```

返回字符串的共有前缀。

```python
>>> from pydu.string import common_prefix
>>> common_prefix(['abcd', 'abc1'])
'abc'
```


## string.common_suffix
```python
common_suffix(l)
```

返回字符串的共有后缀

```python
>>> from pydu.string import common_suffix
>>> common_suffix(['dabc', '1abc'])
'abc'
```


## string.sort
```python
sort(s, reversed=False)
```

对给定的字符串进行排序，默认是升序，如果 `reverse` 的值为 `True`，将以降序排序。

```python
>>> from pydu.string import sort
>>> sort('dabc')
'abcd'
```
