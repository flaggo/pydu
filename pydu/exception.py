import contextlib
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
