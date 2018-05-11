# System

提供处理系统（如追踪文件、创建目录、链接等）的工具。


## system.FileTracker
```python
FileTracker()
```

跟踪当前打开的文件，调用 `FileTracker.track()` 开始跟踪。当打开许多文件时，`FileTracker` 能够跟踪它们，你可以通过调用 `FileTracker.get_openfiles()` 来定位得到这些文件对象。

```python
FiltTracker.track()
```

开始跟踪打开文件。

```python
FiltTracker.untrack()
```

停止跟踪打开文件。

```python
FiltTracker.get_openfiles()
```

获取当前已打开的文件。

```python
>>> from pydu.system import FileTracker
>>> FileTracker.track()
>>> f = open('test', 'w')
>>> FileTracker.get_openfiles()
{<_io.TextIOWrapper name='test' mode='w' encoding='UTF-8'>}
>>> f.close()
>>> FileTracker.get_openfiles()
set()
>>> FileTracker.untrack()
>>> f = open('test', 'w')
>>> FileTracker.get_openfiles()
set()
```


## system.makedirs
```python
makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False)
```

`makedirs` 基于 `os.makedirs` ，它会创建目标文件夹，以及中间文件夹
（当中间文件夹不存在的时候）。 `mode` 默认值为 `0o75`，当被创建的文件夹已经存在的时候，
如果 `eist_ok` 的值为 `False`，`makedirs` 将会抛出异常。
如果 `ignore_errors` 的值为 `True`，所有的异常将会被忽略。

```python
>>> from pydu.system import makedirs
>>> makedirs('test1/test2')
>>> makedirs('test1',exist_ok=True)
>>> makedirs('test1')
Traceback (most recent call last):
...    OSError: Create dir: test1 error.
```

## system.remove
```python
remove(path, mode=0o755, ignore_errors=False, onerror)
```

删除文件或者文件夹。

如果 `ignore_errors` 的值为 `True` ，异常将会被忽略；
否者，如果 `onerror` 的值不为 `None` ，那么 `onerror` 函数将会处理这些异常。
`onerror` 的参数包括 `func` ， `path` 和 `exc_info` 。
`path` 表示 `func` 函数处理该路径时抛出的异常；
`exc_info` 是由 `sys.exc_info` 返回的元组。
如果 `ignore_errors` 为 `False`，并且 `onerror` 的值为 `None`，
则尝试将只读的 `path` 改为可写并尝试删除，若非只读则抛出异常。

```python
>>> from pydu.system import makedirs
>>> from pydu.system import remove
>>> from pydu.system import touch
>>> makedirs('test')
>>> remove('test')
>>> touch('test.txt')
>>> remove('test.txt')
>>> remove('test.txt', ignore_errors=True)
>>> remove('test.txt')
Traceback (most recent call last):
...    OSError: Remove path: test error. Reason: [Errno 2] No such file or directory: 'test.txt'
```

## system.removes
```python
removes(paths, mode=0o755, ignore_errors=False, onerror)
```

删除多个文件或者（和）文件夹，其他的参数见 `remove`。

```python
>>> from pydu.system import makedirs
>>> from pydu.system import remove
>>> from pydu.system import open_file
>>> makedirs('test1')
>>> makedirs('test2')
>>> open_file('test.txt')
>>> removes(['test.txt','test1','test2'])
```

## system.open_file
```python
open_file(path, mode='wb+', buffer_size=-1, ignore_errors=False):
```

默认以 `wb+` 的方式打开文件，如果需要被创建的文件的上级目录不存在，该目录将会被创建。如果 `ignore_errors` 为 `True` ，异常将会被忽略。

```python
>>> from pydu.system import open_file
>>> open_file('test.txt')
>>> ls
test.txt
>>> open_file('test1.txt',mode='r')
Traceback (most recent call last):
...    OSError: Open file: test1.txt error
```

## system.copy
```python
copy(src, dst, ignore_errors=False, follow_symlinks=True):
```

复制源文件（文件夹）到目标文件（文件夹）。当复制的文件夹包含软连接时，
如果 `symlink` 的值为 `True` ，那么在目标文件夹中会创建相应的软连接；
否者将会复制软连接所指向的文件。当复制的文件为软连接的时候，
如果 `symlink` 的值为 `False` ，那么将会创建与软连接指向相同的软连接；
否者，将会复制软连接所指向的文件。

```python
>>> from pydu.system import copy,symlink
>>> from pydu.system import makedirs,open_fle
>>> open_fle('test/test.txt')
>>> symlink('test/test.txt','test/test.link')
>>> copy('test/test.link','test/test_copy1.link')
>>> copy('test/test.link','test/test_copy2.link',follow_symlink=False)
```

## system.touch
```python
touch(path):
```

生成一个新的文件。

```python
>>> from pydu.system import touch
>>> touch('test.txt')
```

## system.symlink
```python
symlink(src, dst, overwrite=False, ignore_errors=False)
```

创建指向源文件的软连接。
如果 `overwrite` 的值为 `True` ，那么已存在的软连接将会被覆盖。

```python
>>> from pydu.system import symlink
>>> symlink('test.txt','test.link')
```

!> `symlink` 只支持 `Unix类` 的系统。

## system.link
```python
link(src, dst, overwrite=False, ignore_errors=False):
```

创建指向源文件的硬连接。
如果 `overwrite` 的值为 `True` ，那么已存在的硬连接将会被覆盖。

```python
>>> from pydu.system import link
>>> link('test.txt','test.link')
```

!> `link` 只支持 `Unix类` 的系统。


## system.which
```python
which(cmd, mode=os.F_OK | os.X_OK, path=None):
```

给定命令名称、模式、和环境变量PATH，返回在PATH下符合给定模式的命令的路径，
如果找不到就返回None。

`mode` 默认是 os.F_OK | os.X_OK。
`path` 默认是 os.environ.get("PATH")的结果，也可被被自定义的搜索路径重载。

在Python 3中，`which` 就是 `shutil.which`。

```python
>>> from pydu.system import which
>>> which('echo')
/bin/echo
```


## system.chmod
```python
chmod(path, mode, recursive=False)
```

将权限改成给定模式。如果 `recursive` 是True，将会递归。

```python
>>> from pydu.system import chmod
>>> chmod('/opt/sometest', 0o744)
>>> oct(os.stat('/opt/sometest').st_mode)[-3:]
'744'
```

!> 尽管Windows支持 `chmod`，但你只能使用它设置文件的只读标志
（通过 tat.S_IWRITE 和 stat.S_IREAD）常量或者相关整数值。
其他所有位会被忽略。


## system.chcp
```python
chcp(code)
```

设置活动代码页号的上下文管理器。它也能够被当做函数使用。

```python
>>> from pydu.system import chcp
>>> chcp(437)
<active code page number: 437>
>>> with chcp(437):
...     pass
>>>
```

!> `chcp` 只能用于 `Windows` 系统。


## system.preferredencoding
```python
preferredencoding(code)
```

以最佳的方式获取系统编码。
