# archive

Utils for archiving files.

## archive.extract
```python
extract(path, to_path='', ext='')
```

Unpack the tar or zip file at the specified path or file to the directory
specified by ``to_path``. It supports many extensions, like ``.tar``,
``.tar.bz2``, ``.tar.gz``, ``.tgz``, ``.tz2``, ``.zip``. If the file name of
given ``path`` doesn't contain file extension, the ``ext`` parameter can be
specified one of supported extensions to indicate file type.

```python
>>> from pydu.archive import extract
>>> extract('foobar.tgz', '/tmp')
>>> extract('foobar', '/tmp', ext='.tgz')
>>> extract('foobar', '/tmp')
Traceback (most recent call last):
  ...    AttributeError: pydu.archive.UnrecognizedArchiveFormat: Path not a recognized archive format: foobar
```
