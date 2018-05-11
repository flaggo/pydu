# Unit

提供处理单位的工具。

## unit.Bytes
```python
Bytes(bytes)
```

提供处理字节的各类方法。

```python
Bytes.convert(self, unit=None, multiple=1024)
```

将字节转化为给定 `unit`。如果 `unit` 是 `None`，将字节转换为合适的单位。
转换 `multiple` 的默认值是 1024。

```python
>>> Bytes(1024).convert()
(1, 'KB')
```
