import contextlib
from functools import wraps
from .compat import PY2


if PY2:
    @contextlib.contextmanager
    def ignore(*exceptions):
        try:
            yield
        except exceptions:
            pass
else:
    ignore = contextlib.suppress


def default_if_except(exception_clses, default=None):
    """
    A exception decorator which excepts given exceptions and
    return default value.
    """
    def _default_if_except(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_clses:
                return default
        return wrapper
    return _default_if_except
