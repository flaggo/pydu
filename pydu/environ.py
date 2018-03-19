import os
from contextlib import contextmanager
from pydu.list import tolist
from pydu.compat import iteritems


@contextmanager
def environ(**kwargs):
    """
    Context manager for updating one or more environment variables.

    Preserves the previous environment variable (if available) and
    recovers when exiting the context manager.

    If given variable_name=None, it means removing the variable from
    environment temporarily.
    """
    original_kwargs = {}

    for key in kwargs:
        original_kwargs[key] = os.environ.get(key, None)
        if kwargs[key] is None and original_kwargs[key] is not None:
            del os.environ[key]
        elif kwargs[key] is not None:
            os.environ[key] = kwargs[key]

    yield

    for key, value in iteritems(original_kwargs):
        if value is None:
            os.environ.pop(key, None)
            continue

        os.environ[key] = value


@contextmanager
def path(append=None, prepend=None, replace=None):
    """
    Context manager for updating the PATH environment variable which
    appends, prepends or replaces the PATH with given string or
    a list of strings.
    """
    original = os.environ['PATH']

    if replace:
        replace = tolist(replace)
        os.environ['PATH'] = os.pathsep.join(replace)
    else:
        if append:
            append = tolist(append)
            append.insert(0, os.environ['PATH'])
            os.environ['PATH'] = os.pathsep.join(append)

        if prepend:
            prepend = tolist(prepend)
            prepend.append(os.environ['PATH'])
            os.environ['PATH'] = os.pathsep.join(prepend)

    yield

    os.environ['PATH'] = original
