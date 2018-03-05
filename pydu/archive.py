"""
Based on "python-archive" -- http://pypi.python.org/pypi/python-archive/
Copyright (c) 2010 Gary Wilson Jr. <gary.wilson@gmail.com> and contributors.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import os
import shutil
import stat
import tarfile
import zipfile

from . import logger
from .compat import string_types


class ArchiveException(Exception):
    """
    Base exception class for all archive errors.
    """


class UnrecognizedArchiveFormat(ArchiveException):
    """
    Error raised when passed file is not a recognized archive format.
    """


def extract(path, dst='', ext=''):
    """
    Unpack the tar or zip file at the specified path or file to the directory
    specified by to_path.
    """
    with Archive(path, ext=ext) as archive:
        archive.extract(dst)


class Archive(object):
    """
    The external API class that encapsulates an archive implementation.
    """
    def __init__(self, file, ext=''):
        """
        Arguments:
        * 'file' can be a string path to a file or a file-like object.
        * Optional 'ext' argument can be given to override the file-type
          guess that is normally performed using the file extension of the
          given 'file'.  Should start with a dot, e.g. '.tar.gz'.
        """
        self._archive = self._archive_cls(file, ext=ext)(file)

    @staticmethod
    def _archive_cls(file, ext=''):
        """
        Return the proper Archive implementation class, based on the file type.
        """
        if isinstance(file, string_types):
            filename = file
        else:
            try:
                filename = file.name
            except AttributeError:
                raise UnrecognizedArchiveFormat(
                    "File object not a recognized archive format.")
        lookup_filename = filename + ext
        base, tail_ext = os.path.splitext(lookup_filename.lower())
        cls = extension_map.get(tail_ext)
        if not cls:
            base, ext = os.path.splitext(base)
            cls = extension_map.get(ext)
        if not cls:
            raise UnrecognizedArchiveFormat(
                "Path not a recognized archive format: %s" % filename)
        return cls

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def extract(self, dst=''):
        self._archive.extract(dst)

    def list(self):
        self._archive.list()

    def filenames(self):
        return self._archive.filenames()

    def close(self):
        self._archive.close()


class BaseArchive(object):
    """
    Base Archive class.  Implementations should inherit this class.
    """
    @staticmethod
    def _copy_permissions(mode, filename):
        """
        If the file in the archive has some permissions (this assumes a file
        won't be writable/executable without being readable), apply those
        permissions to the unarchived file.
        """
        if mode & stat.S_IROTH:
            os.chmod(filename, mode)

    def split_leading_dir(self, path):
        path = str(path)
        path = path.lstrip('/').lstrip('\\')
        if '/' in path and (('\\' in path and path.find('/') < path.find(
                '\\')) or '\\' not in path):
            return path.split('/', 1)
        elif '\\' in path:
            return path.split('\\', 1)
        else:
            return path, ''

    def has_leading_dir(self, paths):
        """
        Returns true if all the paths have the same leading path name
        (i.e., everything is in one subdirectory in an archive)
        """
        common_prefix = None
        for path in paths:
            prefix, rest = self.split_leading_dir(path)
            if not prefix:
                return False
            elif common_prefix is None:
                common_prefix = prefix
            elif prefix != common_prefix:
                return False
        return True

    def extract(self, dst):
        raise NotImplementedError(
            'subclasses of BaseArchive must provide an extract() method')

    def list(self):
        raise NotImplementedError(
            'subclasses of BaseArchive must provide a list() method')

    def filenames(self):
        """
        Return a list of the filenames contained in the archive.
        """
        raise NotImplementedError()

    def __del__(self):
        if hasattr(self, "_archive"):
            self._archive.close()


class TarArchive(BaseArchive):

    def __init__(self, file):
        # tarfile's open uses different parameters for file path vs. file obj.
        if isinstance(file, string_types):
            self._archive = tarfile.open(name=file)
        else:
            self._archive = tarfile.open(fileobj=file)

    def extract(self, dst):
        members = self._archive.getmembers()
        leading = self.has_leading_dir(x.name for x in members)
        for member in members:
            name = member.name
            if leading:
                name = self.split_leading_dir(name)[1]
            filename = os.path.join(dst, name)
            if member.isdir():
                if filename and not os.path.exists(filename):
                    os.makedirs(filename)
            else:
                try:
                    extracted = self._archive.extractfile(member)
                except (KeyError, AttributeError) as exc:
                    # Some corrupt tar files seem to produce this
                    # (specifically bad symlinks)
                    logger.error("In the tar file %s the member %s is invalid: %s",
                                 name, member.name, exc)
                else:
                    dirname = os.path.dirname(filename)
                    if dirname and not os.path.exists(dirname):
                        os.makedirs(dirname)
                    with open(filename, 'wb') as outfile:
                        shutil.copyfileobj(extracted, outfile)
                        self._copy_permissions(member.mode, filename)
                finally:
                    try:
                        extracted.close()
                    except NameError:
                        pass

    def list(self):
        self._archive.list()

    def filenames(self):
        return self._archive.getnames()

    def close(self):
        self._archive.close()


class ZipArchive(BaseArchive):

    def __init__(self, file):
        # ZipFile's 'file' parameter can be path (string) or file-like obj.
        self._archive = zipfile.ZipFile(file)

    def extract(self, dst):
        namelist = self._archive.namelist()
        leading = self.has_leading_dir(namelist)
        for name in namelist:
            data = self._archive.read(name)
            info = self._archive.getinfo(name)
            if leading:
                name = self.split_leading_dir(name)[1]
            filename = os.path.join(dst, name)
            dirname = os.path.dirname(filename)
            if dirname and not os.path.exists(dirname):
                os.makedirs(dirname)
            if filename.endswith(('/', '\\')):
                # A directory
                if not os.path.exists(filename):
                    os.makedirs(filename)
            else:
                with open(filename, 'wb') as outfile:
                    outfile.write(data)
                # Convert ZipInfo.external_attr to mode
                mode = info.external_attr >> 16
                self._copy_permissions(mode, filename)

    def list(self):
        self._archive.printdir()

    def filenames(self):
        return self._archive.namelist()

    def close(self):
        self._archive.close()


extension_map = {
    '.tar': TarArchive,
    '.tar.bz2': TarArchive,
    '.tar.gz': TarArchive,
    '.tgz': TarArchive,
    '.tz2': TarArchive,
    '.zip': ZipArchive,
}
