import os
import sys
import stat
import errno
import shutil
import warnings

from . import logger
from .platform import WINDOWS
from .compat import PY2, builtins


_openfiles = set()
_origin_open = builtins.open
if PY2:
    _origin_file = builtins.file

    class _trackfile(builtins.file):
        def __init__(self, *args):
            self.path = args[0]
            logger.debug('Opening "%s"', self.path)
            super(_trackfile, self).__init__(*args)
            _openfiles.add(self)

        def close(self):
            logger.debug('Closing "%s"', self.path)
            super(_trackfile, self).close()
            _openfiles.remove(self)


    def _trackopen(*args):
        return _trackfile(*args)
else:
    def _trackopen(*args, **kwargs):
        f = _origin_open(*args, **kwargs)
        path = args[0]
        logger.debug('Opening "%s"', path)
        _openfiles.add(f)

        origin_close = f.close

        def close():
            logger.debug('Closing "%s"', path)
            origin_close()
            _openfiles.remove(f)
        f.close = close
        return f


class FileTracker(object):
    @staticmethod
    def track():
        builtins.open = _trackopen
        if PY2:
            builtins.file = _trackfile

    @staticmethod
    def untrack():
        builtins.open = _origin_open
        if PY2:
            builtins.file = _origin_file

    @staticmethod
    def get_openfiles():
        return _openfiles


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
    except:
        if not ignore_errors:
            raise OSError('Create dir: {!r} error.'.format(path))


def remove(path, ignore_errors=False, onerror=None):
    """
    Remove a file or directory.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is False and onerror is None, it attempts to set path as writeable and
    then proceed with deletion if path is read-only, or raise an exception
    if path is not read-only.
    """
    if ignore_errors:
        def onerror(func, path, exc):
            pass
    elif onerror is None:
        def onerror(func, path, exc):
            try:
                if (os.stat(path).st_mode & stat.S_IREAD) or not os.access(path, os.W_OK):
                    os.chmod(path, stat.S_IWRITE | stat.S_IWUSR)
                    func(path)
                else:
                    exc_type, exc_exception, exc_tb = exc
                    raise exc_exception
            except Exception as e:
                raise OSError('Remove path: {!r} error. Reason: {}'.format(path, e))

    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=ignore_errors, onerror=onerror)
    else:
        try:
            os.remove(path)
        except:
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
    except:
        if not ignore_errors:
            raise OSError('Open file: {!r} error'.format(path))
    return f


def copy(src, dst, ignore_errors=False, follow_symlinks=True):
    """
    Copy data and mode bits ("cp src dst").

    Both the source and destination may be a directory.

    When copy a directory,which contains a symlink, If the optional
    symlinks flag is true, symbolic links in the source tree result
    in symbolic links in the destination tree; if it is false, the
    contents of the files pointed to by symbolic links are copied.
    If the file pointed by the symlink doesn't exist, an exception
    will be raise.

    When copy a file,if follow_symlinks is false and src is a symbolic
    link, a new symlink will be created instead of copying the file it
    points to,else the contents of the file pointed to by symbolic links
    is copied.

    If source and destination are the same file, a SameFileError will be
    raised.

    If ignore_errors is set, errors are ignored.
    """
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst, symlinks=follow_symlinks)
        else:
            if not follow_symlinks and os.path.islink(src):
                os.symlink(os.readlink(src), dst)
            else:
                shutil.copy(src, dst)
    except:
        if not ignore_errors:
            raise OSError('Copy {!r} to {!r} error'.format(src, dst))


def touch(path):
    """
    Open a file as write,and then close it.
    """
    with open(path, 'w'):
        pass


def chmod(path, mode, recursive=False):
    """
    Change permissions to the given mode.
    If `recursive` is True perform recursively.

        >>> chmod('/opt/sometest', 0o755)
        >>> oct(os.stat('/opt/sometest').st_mode)[-3:]
        755
    """
    chmod_ = os.chmod
    if recursive and os.path.isdir(path):
        for dirpath, _, filenames in os.walk(path):
            chmod_(dirpath, mode)
            for filename in filenames:
                chmod_(os.path.join(dirpath, filename), mode)
    else:
        os.chmod(path, mode)


if PY2:
    # shutil.which from Python3
    def which(cmd, mode=os.F_OK | os.X_OK, path=None):
        """
        Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.

        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.
        """
        # Check that a given file can be accessed with the correct mode.
        # Additionally check that `file` is not a directory, as on Windows
        # directories pass the os.access check.
        def _access_check(fn, mode):
            return (os.path.exists(fn) and os.access(fn, mode)
                    and not os.path.isdir(fn))

        # If we're given a path with a directory part, look it up directly rather
        # than referring to PATH directories. This includes checking relative to the
        # current directory, e.g. ./script
        if os.path.dirname(cmd):
            if _access_check(cmd, mode):
                return cmd
            return None

        if path is None:
            path = os.environ.get("PATH", os.defpath)
        if not path:
            return None
        path = path.split(os.pathsep)

        if WINDOWS:
            # The current directory takes precedence on Windows.
            if not os.curdir in path:
                path.insert(0, os.curdir)

            # PATHEXT is necessary to check on Windows.
            pathext = os.environ.get("PATHEXT", "").split(os.pathsep)
            # See if the given file matches any of the expected path extensions.
            # This will allow us to short circuit when given "python.exe".
            # If it does match, only test that one, otherwise we have to try
            # others.
            if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
                files = [cmd]
            else:
                files = [cmd + ext for ext in pathext]
        else:
            # On other platforms you don't have things like PATHEXT to tell you
            # what file suffixes are executable, so just pass on cmd as-is.
            files = [cmd]

        seen = set()
        for dir in path:
            normdir = os.path.normcase(dir)
            if not normdir in seen:
                seen.add(normdir)
                for thefile in files:
                    name = os.path.join(dir, thefile)
                    if _access_check(name, mode):
                        return name
        return None
else:
    which = shutil.which


if WINDOWS:
    # For Windows system
    from ctypes import windll

    class chcp(object):
        """
        Context manager which sets the active code page number.
        It could also be used as function.
        """
        def __init__(self, code):
            self.origin_code = windll.kernel32.GetConsoleOutputCP()
            self.code = code
            windll.kernel32.SetConsoleOutputCP(code)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            windll.kernel32.SetConsoleOutputCP(self.origin_code)

        def __repr__(self):
            return '<active code page number: {}>'.format(self.code)
else:
    # For non Windows system
    def symlink(src, dst, overwrite=False, ignore_errors=False):
        """
        Create a symbolic link pointing to source named link_name.

        If dist is exist and overwrite is true,a new symlink will be created

        If ignore_errors is set, errors are ignored.
        """
        try:
            if os.path.exists(dst):
                if overwrite:
                    remove(dst)
                else:
                    return
            os.symlink(src, dst)
        except Exception:
            if not ignore_errors:
                raise OSError('Link {!r} to {!r} error'.format(dst, src))


    def link(src, dst, overwrite=False, ignore_errors=False):
        """
        Create a hard link pointing to source named link_name.

        If dist is exist and overwrite is true,a new symlink will be created

        If ignore_errors is set, errors are ignored.
        """
        try:
            if os.path.exists(dst):
                if overwrite:
                    remove(dst)
                else:
                    return
            os.link(src, dst)
        except:
            if not ignore_errors:
                raise OSError('Link {!r} to {!r} error'.format(dst, src))
