import os
from pydu.compat import iteritems
from contextlib import contextmanager


@contextmanager
def environ(**kwargs):
    """
    Context manager for updating one or more environment variables.

    Preserves the previous environment variable (if available) and
    recovers when exiting the context manager.
    """
    original_kwargs = {}

    for key in kwargs:
        original_kwargs[key] = os.environ.get(key, None)
        os.environ[key] = kwargs[key]

    yield

    for key, value in iteritems(original_kwargs):
        if value is None:
            del os.environ[key]
            continue

        os.environ[key] = value
