# Convert

Utils for converting one type of data to another.


## convert.boolean
```python
boolean(obj)
```

Convert obj to a boolean value.

If obj is string, obj will converted by case-insensitive way:

* convert `yes`, `y`, `on`, `true`, `t`, `1` to True
* convert `no`, `n`, `off`, `false`, `f`, `0` to False
* raising TypeError if other values passed

If obj is non-string, obj will converted by `bool(obj)`.

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

Convert binary string to octal string.
For instance: '1001' -> '11'

```python
>>> from pydu.convert import bin2oct
>>> bin2oct('1001')
'11'
```


## convert.bin2dec
```python
bin2dec(x)
```

Convert binary string to decimal number.
For instance: '11' -> 3

```python
>>> from pydu.convert import bin2dec
>>> bin2dec('11')
3
```


## convert.bin2hex
```python
bin2hex(x)
```

Convert binary string to hexadecimal string.
For instance: '11010' -> '1a'

```python
>>> from pydu.convert import bin2hex
>>> bin2hex('11010')
'1a'
```


## convert.oct2bin
```python
oct2bin(x)
```

Convert octal string to binary string.
For instance: '11' -> '1001'

```python
>>> from pydu.convert import oct2bin
>>> oct2bin('11')
'1001'
```


## convert.oct2dec
```python
oct2dec(x)
```

Convert octal string to decimal number.
For instance: '11' -> 9

```python
>>> from pydu.convert import oct2dec
>>> oct2dec('11')
9
```


## convert.oct2hex
```python
oct2hex(x)
```

Convert octal string to hexadecimal string.
For instance: '32' -> '1a'

```python
>>> from pydu.convert import oct2hex
>>> oct2hex('32')
'1a'
```


## convert.dec2bin
```python
dec2bin(x)
```

Convert decimal number to binary string.
For instance: 3 -> '11'

```python
>>> from pydu.convert import dec2bin
>>> dec2bin(3)
'11'
```


## convert.dec2oct
```python
dec2oct(x)
```

Convert decimal number to octal string.
For instance: 9 -> '11'

```python
>>> from pydu.convert import dec2oct
>>> dec2oct(9)
'11'
```


## convert.dec2hex
```python
dec2hex(x)
```

Convert decimal number to hexadecimal string.
For instance: 26 -> '1a'

```python
>>> from pydu.convert import dec2hex
>>> dec2hex(26)
'1a'
```


## convert.hex2bin
```python
hex2bin(x)
```

Convert hexadecimal string to binary string.
For instance: '1a' -> '11010'

```python
>>> from pydu.convert import hex2bin
>>> hex2bin('1a')
'11010'
```


## convert.hex2oct
```python
hex2oct(x)
```

Convert hexadecimal string to octal string.
For instance: '1a' -> '32'

```python
>>> from pydu.convert import hex2oct
>>> hex2oct('1a')
'32'
```


## convert.hex2dec
```python
hex2dec(x)
```

Convert hexadecimal string to decimal number.
For instance: '1a' -> 26

```python
>>> from pydu.convert import hex2dec
>>> hex2dec('1a')
26
```
