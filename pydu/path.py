import os
from contextlib import contextmanager


@contextmanager
def cd(path):
    """
    Context manager for cd the given path.
    """
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)
