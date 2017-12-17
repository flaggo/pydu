from contextlib import contextmanager


@contextmanager
def ignore(*exceptions):
    try:
        yield
    except exceptions:
        pass
