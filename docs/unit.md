# Unit

Utils for handling unit.

## unit.Bytes
```python
Bytes(bytes)
```

Supply several methods dealing with bytes.

```python
Bytes.convert(self, unit=None, multiple=1024)
```

Convert bytes with given `unit`.
If `unit` is `None`, convert bytes with suitable unit.
Convert `multiple` is default to be 1024.

```python
>>> Bytes(1024).convert()
(1, 'KB')
```
