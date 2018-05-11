# path

提供处理路径的工具。

## path.cd
```python
cd(path)
```

进入到给定目录的上下文管理器。

```python
>>> from pydu.path import cd
>>> with cd('test'):
...     pass
```


## path.is_super_path
```python
is_super_path(path1, path2)
```

判断 `path1` 是否是 `path2` 的父路径（或父父路径等）。
注意如果 `path1` 和 `path2` 一样，它也被视作是 `path2` 的父路径。

比如，\"/\"、\"opt\"或者\"/opt/test\"是\"/opt/test\"的超级父路径，
而\"/opt/t\"则不是。

```python
>>> from pydu.path import is_super_path
>>> is_super_path('/aa/bb/cc', '/aa/bb/cc')
True
>>> is_super_path('/aa/bb', '/aa/bb/cc')
True
>>> is_super_path('/aa/b', '/aa/bb/cc')
False
```


## path.normjoin
```python
normjoin(path)
```

将一个或多个路径联接，并将之标准化。

```python
>>> from pydu.path import normjoin
>>> normjoin('/a', '../b')
'/b'
```


## path.filename
```python
filename(path)
```

返回没有扩展名的文件名。

```python
>>> from pydu.path import filename
>>> filename('/foo/bar.ext')
'bar'
```


## path.fileext
```python
fileext(path)
```

返回文件扩展名。
如果文件没有扩展名，则返回空字符串。

```python
>>> from pydu.path import fileext
>>> filename('/foo/bar.ext')
'.ext'
```
