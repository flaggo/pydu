# Convert

提供将一类数据转换为另一类的工具。


## convert.boolean
```python
boolean(obj)
```

将对象转换为布尔值。

如果对象是字符串，将会以不区分大小写的形式转换：

* 将 `yes`、 `y`、 `on`、 `true`、 `t`、 `1` 转换为True
* 将 `no`、 `n`、 `off`、 `false`、 `f`、 `0` 转换为False
* 如果传入其他值，抛出TypeError

如果对象不是字符串，将会使用 `bool(obj)` 转换。

```python
>>> from pydu.string import boolean
>>> boolean('yes')
True
>>> boolean('no')
False
```


## convert.bin2oct
```python
bin2oct(x)
```

把二进制字符串转换为八进制字符串。
比如：'1001' -> '11'

```python
>>> from pydu.convert import bin2oct
>>> bin2oct('1001')
'11'
```


## convert.bin2dec
```python
bin2dec(x)
```

把二进制字符串转换为十进制数字。
比如：'11' -> 3

```python
>>> from pydu.convert import bin2dec
>>> bin2dec('11')
3
```


## convert.bin2hex
```python
bin2hex(x)
```

把二进制字符串转换为十六进制字符串。
比如：'11010' -> '1a'

```python
>>> from pydu.convert import bin2hex
>>> bin2hex('11010')
'1a'
```


## convert.oct2bin
```python
oct2bin(x)
```

把八进制字符串转换为二进制字符串。
比如：'11' -> '1001'

```python
>>> from pydu.convert import oct2bin
>>> oct2bin('11')
'1001'
```


## convert.oct2dec
```python
oct2dec(x)
```

把八进制字符串转换为十进制数字。
比如：'11' -> 9

```python
>>> from pydu.convert import oct2dec
>>> oct2dec('11')
9
```


## convert.oct2hex
```python
oct2hex(x)
```

把八进制字符串转换为十六进制字符串。
比如：'32' -> '1a'

```python
>>> from pydu.convert import oct2hex
>>> oct2hex('32')
'1a'
```


## convert.dec2bin
```python
dec2bin(x)
```

把十进制数字转换为二进制字符串。
比如：3 -> '11'

```python
>>> from pydu.convert import dec2bin
>>> dec2bin(3)
'11'
```


## convert.dec2oct
```python
dec2oct(x)
```

把十进制数字转换为八进制字符串。
比如：9 -> '11'

```python
>>> from pydu.convert import dec2oct
>>> dec2oct(9)
'11'
```


## convert.dec2hex
```python
dec2hex(x)
```

把十进制数字转换为十六进制字符串。
比如：26 -> '1a'

```python
>>> from pydu.convert import dec2hex
>>> dec2hex(26)
'1a'
```


## convert.hex2bin
```python
hex2bin(x)
```

把十六进制字符串转换为二进制字符串。
比如：'1a' -> '11010'

```python
>>> from pydu.convert import hex2bin
>>> hex2bin('1a')
'11010'
```


## convert.hex2oct
```python
hex2oct(x)
```

把十六进制字符串转换为八进制字符串。
比如：'1a' -> '32'

```python
>>> from pydu.convert import hex2oct
>>> hex2oct('1a')
'32'
```


## convert.hex2dec
```python
hex2dec(x)
```

把十六进制字符串转换为十进制数字。
比如：'1a' -> 26

```python
>>> from pydu.convert import hex2dec
>>> hex2dec('1a')
26
```
