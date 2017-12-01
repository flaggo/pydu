import os
import sys
import shutil


# todo tests and docs
def makedirs(path, mode=0o755, ignore_errors=False, exist_ok=False):
    if exist_ok and os.path.exists(path):
        return
    try:
        os.makedirs(path, mode)
    except Exception:
        if not ignore_errors:
            raise OSError('Create dir: {} error.')


def remove(path, ignore_errors=False, onerror=None):
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
    for path in paths:
        remove(path, ignore_errors=ignore_errors, onerror=onerror)


def open_file(path, mode='wb+', buffer_size=-1, ignore_errors=False):
    f = None
    try:
        if path and not os.path.isdir(path):
            makedirs(os.path.dirname(path))
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


def copy(src, dst, ignore_errors=False, follow_symlinks=True):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst, symlinks=not follow_symlinks)
        else:
            shutil.copy(src, dst, follow_symlinks=follow_symlinks)
    except Exception:
        if not ignore_errors:
            raise OSError('Copy {} to {} error'.format(src, dst))
