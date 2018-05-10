# process

Utils for handling processes.

`process` is based on `psutil`. Need to `pip install psutil` first.


## process.get_processes_by_path
```python
get_processes_by_path(path)
```

Get processes which are running on given path or sub path of given path.

```python
>>> from pydu.process import get_processes_by_path
>>> get_processes_by_path('/usr/bin/python')
[{'cmdline': '/usr/bin/python2.7', 'pid': 23383, 'name': 'python'}]
```

