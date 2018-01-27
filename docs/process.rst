Process
-------

.. py:function:: pydu.process.get_processes_by_path(path)

    Get processes which are running on given path or sub path of given path.

    >>> from pydu.process import get_processes_by_path
    >>> get_processes_by_path('/usr/bin/python')
    [{'cmdline': '/usr/bin/python2.7', 'pid': 23383, 'name': 'python'}]
