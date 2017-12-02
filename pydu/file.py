import os
import sys
import shutil


# todo tests and docs
def makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False):
    """
    Create a leaf directory and all intermediate ones.

    Based on os.makedirs, but also supports ignore_errors which will
    ignore all errors raised by os.makedirs.
    """
    if exist_ok and os.path.exists(path):
        return
    try:
        os.makedirs(path, mode)
    except Exception:
        if not ignore_errors:
            raise OSError('Create dir: {} error.')


def remove(path, ignore_errors=False, onerror=None):
    """
    Remove a file or directory.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is False and onerror is None, an exception is raised.
    """
    if ignore_errors:
        def onerror(*args):
            pass
    elif onerror is None:
        def onerror(*args):
            raise OSError('Remove path: {} error'.format(path))

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=ignore_errors, onerror=onerror)
    else:
        try:
            os.remove(path)
        except Exception:
            onerror(os.remove, path, sys.exc_info())


def removes(paths, ignore_errors=False, onerror=None):
    """
    Remove a list of file and/or directory.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is False and onerror is None, an exception is raised.
    """
    for path in paths:
        remove(path, ignore_errors=ignore_errors, onerror=onerror)


def open_file(path, mode='wb+', buffer_size=-1, ignore_errors=False):
    """
    Open a file, defualt mode 'wb+'.

    If path not exists, it will be created automatically.
    If ignore_errors is set, errors are ignored.
    """
    f = None
    try:
        if path and not os.path.isdir(path):
            makedirs(os.path.dirname(path), exist_ok=True)
            f = open(path, mode, buffer_size)
    except Exception:
        if not ignore_errors:
            raise OSError('Open file: {} error'.format(path))
    return f


def link(src, dst, overwrite=False, ignore_errors=False):
    try:
        if os.path.exists(dst):
            if overwrite:
                remove(dst)
            else:
                return
        os.link(src, dst)
    except Exception:
        if not ignore_errors:
            raise OSError('Link {} to {} error'.format(dst, src))


def symlink(src, dst, overwrite=False, ignore_errors=False):
    try:
        if os.path.exists(dst):
            if overwrite:
                remove(dst)
            else:
                return
        os.symlink(src, dst)
    except Exception:
        if not ignore_errors:
            raise OSError('Link {} to {} error'.format(dst, src))


def copy(src, dst, ignore_errors=False, follow_symlinks=True):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst, symlinks=follow_symlinks)
        else:
            if not follow_symlinks and os.path.islink(src):
                os.symlink(os.readlink(src), dst)
            else:
                shutil.copy(src, dst)
    except Exception:
        if not ignore_errors:
            raise OSError('Copy {} to {} error'.format(src, dst))
