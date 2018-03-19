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


def is_super_path(path1, path2):
    """
    Whether `path1` is the super path of `path2`.
    Note that if `path1` is same as `path2`, it's also regarded as
    the super path os `path2`.
    For instance "/", "/opt" and "/opt/test" are all the super paths of "/opt/test",
    while "/opt/t" is the super path of "/opt/test".
    """
    path1 = os.path.normpath(path1)
    current_path2 = os.path.normpath(path2)
    parent_path2 = os.path.dirname(current_path2)
    if path1 == current_path2:
        return True

    while parent_path2 != current_path2:
        if path1 == parent_path2:
            return True
        current_path2 = parent_path2
        parent_path2 = os.path.dirname(parent_path2)

    return False


def normjoin(path, *paths):
    """Join one or more path components intelligently and normalize it."""
    return os.path.normpath(os.path.join(path, *paths))
