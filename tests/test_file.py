import os
from pydu.file import makedirs,remove
from pydu.file import removes,open_file
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
        filename = str(tmpdir.join('test.txt'))
        open(filename, 'w')
        remove(filename)
        assert not os.path.exists(filename)

    def test_remove_mutil_dirs(self, tmpdir):
        path = str(tmpdir.join('test/test'))
        makedirs(path)
        path = str(tmpdir.join('test'))
        remove(path)
        assert not os.path.exists(path)

    def test_remove_with_ignore_error(self, tmpdir):
        path = str(tmpdir.join('test'))
        remove(path, ignore_errors=True)

    def test_remove_without_ignore_error(self, tmpdir):
        path = str(tmpdir.join('test'))
        with pytest.raises(Exception) as e:
            remove(path, ignore_errors=False)

    def test_remove_without_ignore_error_with_onerror(self):
        pass


class Testremoves():
    def test_removes_paths(self, tmpdir):
        path1 = str(tmpdir.join('test1'))
        path2 = str(tmpdir.join('test2'))
        path3 = str(tmpdir.join('test3'))
        for path in [path1, path2, path3]:
            makedirs(path)
        removes([path1, path2, path3])
        assert not os.path.exists(path1)
        assert not os.path.exists(path2)
        assert not os.path.exists(path3)

    def test_removes_files(self,tmpdir):
        f1 = str(tmpdir.join('test1.txt'))
        f2 = str(tmpdir.join('test2.txt'))
        f3 = str(tmpdir.join('test3.txt'))
        for f in [f1, f2, f3]:
            open(f, 'w')
        removes([f1, f2, f3])
        for f in [f1, f2, f3]:
            assert not os.path.exists(f)

    def test_removes_files_and_path(self,tmpdir):
        f1 = str(tmpdir.join('test1.txt'))
        f2 = str(tmpdir.join('test2.txt'))
        p1 = str(tmpdir.join('test1'))
        p2 = str(tmpdir.join('test2'))
        for f in [f1,f2]:
            open(f, 'w')
        for p in [p1,p2]:
            makedirs(p)
        removes([f1, f2, p1, p2])
        for f in [f1, f2, p1, p2]:
            assert not os.path.exists(f)


class Testopenfile():
    def test_open_file_without_parent_dir(self,tmpdir):
        f = str(tmpdir.join('test/test1.txt'))
        open_file(f)
        assert os.path.exists(f)

    def test_open_file_in_exist_path(self, tmpdir):
        f = str(tmpdir.join('test2.txt'))
        open_file(f)
        assert os.path.exists(f)

    def test_open_exist_file(self,tmpdir):
        f = str(tmpdir.join('test3.txt'))
        open_file(f)
        with open(f, 'r') as f:
            with pytest.raises(Exception) as f:
                os.remove(f)

    def test_open_file_with_ignore_error(self, tmpdir):
        f = str(tmpdir.join('test1.txt'))
        open_file(f, mode='r', ignore_errors=True)

    def test_open_file_without_ignore_error(self,tmpdir):
        f = str(tmpdir.join('test1.txt'))
        with pytest.raises(Exception) as e:
            open_file(f, mode='r')


class Testlink():
    def test_link_a_file(self, tmpdir):
        pass

    def test_link_a_dir(self, tmpdir):
        pass

    def test_link_with_overwrite(self,tmpdir):
        pass

    def test_link_without_link(self,tmpdir):
        pass

    def test_link_with_ignore_error(self,tmpdir):
        pass

    def test_link_without_error(self,tmpdir):
        pass

