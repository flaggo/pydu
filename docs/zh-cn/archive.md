# archive

提供归档相关工具，如解压。

## archive.extract
```python
extract(path, to_path='', ext='')
```

解压tar或zip文件，可指定 ``to_path`` 解压到特定目录。它支持很多文件格式，包括 "
"``.tar``、``.tar.bz2``、``.tar.gz``、``.tgz``、``.tz2``、``.zip``。如果给定的 "
"``path`` 不包含文件格式，则可指定 ``ext`` 参数来说明文件格式。

```python
>>> from pydu.archive import extract
>>> extract('foobar.tgz', '/tmp')
>>> extract('foobar', '/tmp', ext='.tgz')
>>> extract('foobar', '/tmp')
Traceback (most recent call last):
  ...    AttributeError: pydu.archive.UnrecognizedArchiveFormat: Path not a recognized archive format: foobar
```
