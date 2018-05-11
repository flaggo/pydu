# list

提供处理列表的工具。

## list.uniq
```python
uniq(seq, key=None)
```

从列表中删除重复的元素，同时保留其余的顺序。

可选参数 `key` 的值应该是一个函数，它接受一个参数并返回一个 `key` 来测试唯一性。

```python
>>> from pydu.list import uniq
>>> uniq([1, 4, 0, 2, 0, 3])
[1, 4, 0, 2, 3]
```


## list.tolist
```python
tolist(obj)
```

将给定的 `obj` 转换为列表。

如果 `obj` 不是列表，返回 `[obj]`，否则返回 `obj` 本身。

```python
>>> from pydu.list import tolist
>>> tolist('foo')
['foo']
```


## list.flatten
```python
flatten(seq)
```

生成给定 `seq` 中的每个元素。如果元素是可迭代的并且不是字符串，
就递归 `yield` 元素中的每个子元素。

```python
>>> from pydu.list import flatten
>>> flatten([1, [2, [3, 4]]])
[1, 2, 3, 4]
```
