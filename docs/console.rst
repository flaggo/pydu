Console
-------

.. class:: pydu.console.console_size()

    For Windows, return (width, height) of available window area, (80, 25)
    if no console is allocated.
    For POSIX system, return (width, height) of console terminal. (80, 25)
    on IOError, i.e. when no console is allocated.
    For other system, return (80, 25).

    >>> from pydu.console import console_size
    >>> console_size()
    (80, 25)
