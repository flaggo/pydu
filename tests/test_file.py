import os
import pytest
from pydu.platform import WINDOWS
from pydu.file import makedirs, remove, removes, open_file, copy, touch

if not WINDOWS:
    from pydu.file import link


class TestMakeDirs:
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


def test_touch(tmpdir):
    path = str(tmpdir.join('test'))
    touch(path)
    assert os.path.isfile(path)


@pytest.mark.skipIf(WINDOWS)
class TestLink:
    def test_link(self, tmpdir):
        src = str(tmpdir.join('src'))
        dst = str(tmpdir.join('dst'))
        touch(src)
        link(src, dst)
        assert os.path.exists(dst)
