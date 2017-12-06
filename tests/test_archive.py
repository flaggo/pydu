# coding: utf-8
import os
import shutil
import tempfile
import unittest
from os.path import isfile, join as pathjoin

from pydu.archive import extract, UnrecognizedArchiveFormat


TEST_DIR = os.path.dirname(os.path.realpath(__file__))


class TempDirMixin(object):
    """
    Mixin class for TestCase subclasses to set up and tear down a temporary
    directory for unpacking archives during tests.
    """

    def setUp(self):
        """
        Create temporary directory for testing extraction.
        """
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(TEST_DIR)

    def tearDown(self):
        """
        Clean up temporary directory.
        """
        shutil.rmtree(self.tmpdir)

    def check_files(self, tmpdir):
        self.assertTrue(isfile(pathjoin(tmpdir, '1')))
        self.assertTrue(isfile(pathjoin(tmpdir, '2')))
        self.assertTrue(isfile(pathjoin(tmpdir, 'foo', '1')))
        self.assertTrue(isfile(pathjoin(tmpdir, 'foo', '2')))
        self.assertTrue(isfile(pathjoin(tmpdir, 'foo', 'bar', '1')))
        self.assertTrue(isfile(pathjoin(tmpdir, 'foo', 'bar', '2')))


class ArchiveTester(TempDirMixin):
    """
    A mixin class to be used for testing many Archive methods for a single
    archive file.
    """

    archive = None
    ext = ''

    def setUp(self):
        super(ArchiveTester, self).setUp()
        self.archive_path = pathjoin(TEST_DIR, 'files', self.archive)

    def test_extract(self):
        extract(self.archive_path, self.tmpdir, ext=self.ext)
        self.check_files(self.tmpdir)

    def test_extract_fileobject(self):
        with open(self.archive_path, 'rb') as f:
            extract(f, self.tmpdir, ext=self.ext)
            self.check_files(self.tmpdir)

    def test_extract_no_to_path(self):
        cur_dir = os.getcwd()
        os.chdir(self.tmpdir)
        extract(self.archive_path, ext=self.ext)
        self.check_files(self.tmpdir)
        os.chdir(cur_dir)

    def test_extract_bad_fileobject(self):
        class File:
            pass
        f = File()
        self.assertRaises(UnrecognizedArchiveFormat, extract,
                          (f, self.tmpdir), {'ext': self.ext})


class TestZip(ArchiveTester, unittest.TestCase):
    archive = 'foobar.zip'


class TestTar(ArchiveTester, unittest.TestCase):
    archive = 'foobar.tar'


class TestGzipTar(ArchiveTester, unittest.TestCase):
    archive = 'foobar.tar.gz'


class TestBzip2Tar(ArchiveTester, unittest.TestCase):
    archive = 'foobar.tar.bz2'


class TestNonAsciiNamedTar(ArchiveTester, unittest.TestCase):
    archive = u'压缩.tgz'


class TestUnicodeNamedZip(ArchiveTester, unittest.TestCase):
    archive = u'压缩.zip'


class TestExplicitExt(ArchiveTester, unittest.TestCase):
    archive = 'foobar_tar_gz'
    ext = '.tar.gz'
