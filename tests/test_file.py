import os
from pydu.file import makedirs,remove
import pytest


class Testmakedirs():
    def test_makedirs(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)
        assert os.path.exists(path)

    def test_makedirs_with_exists_path(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)

        makedirs(path, exist_ok=True)

        with pytest.raises(Exception):
            makedirs(path, exist_ok=False)

    def test_makedirs_with_ignore_error(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)
        makedirs(path, ignore_errors=True)

    def test_makedirs_without_ignore_error(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)
        with pytest.raises(Exception):
            makedirs(path, ignore_errors=False, exist_ok=False)

    def test_makedirs_with_mutl_dirs(self, tmpdir):
        path = str(tmpdir.join('test/test'))
        makedirs(path)
        assert os.path.exists(path)

class Testremove():
    def test_remove_dir(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)
        remove(path)
        assert not os.path.exists(path)

    def test_remove_file(self, tmpdir):
        file = str(tmpdir.join('test.txt'))
        open(file, 'w')
        remove(file)
        assert not os.path.exists(file)

    def test_remove_mutil_dirs(self, tmpdir):
        path = str(tmpdir.join('test/test'))
        makedirs(path)
        path = str(tmpdir.join('test'))
        remove(path)
        assert not os.path.exists(path)

    def test_remove_with_ignore_error(self):
        pass

    def test_remove_without_ignore_error(self):
        pass
