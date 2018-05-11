# path

Utils for handling path.

## path.cd
```python
cd(path)
```

Context manager for cd the given path.

```python
>>> from pydu.path import cd
>>> with cd('test'):
...     pass
```


## path.is_super_path
```python
is_super_path(path1, path2)
```

Whether `path1` is the super path of `path2`.
Note that if `path1` is same as `path2`, it's also regarded as
the super path os `path2`.

For instance "/", "/opt" and "/opt/test" are all the super paths of "/opt/test",
while "/opt/t" is the super path of "/opt/test".

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

Join one or more path components intelligently and normalize it.

```python
>>> from pydu.path import normjoin
>>> normjoin('/a', '../b')
'/b'
```


## path.filename
```python
filename(path)
```

Return the filename without extension.

```python
>>> from pydu.path import filename
>>> filename('/foo/bar.ext')
'bar'
```


## path.fileext
```python
fileext(path)
```

Return the file extension.
If file has not extension, return empty string.

```python
>>> from pydu.path import fileext
>>> filename('/foo/bar.ext')
'.ext'
```
