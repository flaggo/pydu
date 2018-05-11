# process

提供处理进程的工具。

`process` 的实现基于 `psutil`。需要先 `pip install psutil`。


## process.get_processes_by_path
```python
get_processes_by_path(path)
```

获取占用给定路径或者其子路径的进程。

```python
>>> from pydu.process import get_processes_by_path
>>> get_processes_by_path('/usr/bin/python')
[{'cmdline': '/usr/bin/python2.7', 'pid': 23383, 'name': 'python'}]
```
