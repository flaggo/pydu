import os
from pydu.file import makedirs,remove,link
from pydu.file import removes,open_file,copy
import pytest
import sys


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


@pytest.mark.skipif(sys.platform == 'win32',
                    reason="does not run on windows")
class Testlink():
    def test_link_a_file(self, tmpdir):
        file = str(tmpdir.join('test.txt'))
        link_file = str(tmpdir.join('test.link'))
        open(file)
        link(file, link_file)
        assert os.path.exists(link_file)

    def test_link_a_dir(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname)
        assert os.path.exists(link_dirname)

    def test_link_with_overwrite(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname)
        link(dirname, link_dirname, overwrite=True)
        assert os.path.exists(link_dirname)

    def test_link_without_overwrite(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname)
        with pytest.raises(Exception) as e:
            link(dirname, link_dirname)

    def test_link_with_ignore_error(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname)
        link(dirname, link_dirname, ignore_errors=True)

    def test_link_without_ignore_error(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname)
        with pytest.raises(Exception) as e:
            link(dirname, link_dirname)


class Testcopy():
    def test_copy_file(self,tmpdir):
        f = str(tmpdir.join('test.txt'))
        f_copy = str(tmpdir.join('test_copy.txt'))
        open(f, 'w')
        copy(f, f_copy)
        assert os.path.exists(f_copy)

    def test_copy_non_empty_dir(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        d_copy = str(tmpdir.join('test_copy'))
        os.makedirs(d)
        open(f, 'w')
        copy(d, d_copy)
        assert os.path.exists(d_copy)

    def test_copy_empty_dir(self,tmpdir):
        d = str(tmpdir.join('test'))
        d_copy = str(tmpdir.join('test_copy'))
        makedirs(d)
        copy(d,d_copy)
        assert os.path.exists(d_copy)

    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    def test_copy_dir_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        link_f = str(tmpdir.join('test/test_link.txt'))
        d_copy = str(tmpdir.join('test_copy'))
        new_link_f = str(tmpdir.join('test_copy/test_link.txt'))
        open(f)
        os.symlink(f, link_f)
        copy(d, d_copy, follow_symlinks=True)
        assert os.path.exists(d_copy)
        assert os.path.islink(new_link_f)

    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    def test_copy_dir_not_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        link_f = str(tmpdir.join('test/test_link.txt'))
        d_copy = str(tmpdir.join('test_copy'))
        new_link_f = str(tmpdir.join('test_copy/test_link.txt'))
        open(f)
        os.symlink(f, link_f)
        copy(d, d_copy)
        assert os.path.exists(d_copy)
        assert not os.path.islink(new_link_f)

    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    def test_copy_file_follow_symlink(self, tmpdir):
        file = str(tmpdir.join('test.txt'))
        link_file = str(tmpdir.join('test.link'))
        copy_link_file = str(tmpdir.join('test_copy.link'))
        open(file)
        link(file, link_file)
        copy(link_file, copy_link_file,follow_symlinks=True)
        assert os.path.exists(copy_link_file)
        assert not os.path.islink(copy_link_file)

    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    def test_copy_file_not_follow_symlink(self, tmpdir):
        file = str(tmpdir.join('test.txt'))
        link_file = str(tmpdir.join('test.link'))
        copy_link_file = str(tmpdir.join('test_copy.link'))
        open(file)
        link(file, link_file)
        copy(link_file, copy_link_file, follow_symlinks=False)
        assert os.path.exists(copy_link_file)
        assert os.path.islink(copy_link_file)

    def test_copy_path_to_exits_path(self, tmpdir):
        dir1 = str(tmpdir.join('test1'))
        dir2 = str(tmpdir.join('test2'))
        makedirs(dir1)
        makedirs(dir2)
        with pytest.raises(Exception) as e:
            copy(dir1, dir2)

    def test_copy_without_ignore_error(self, tmpdir):
        dir1 = str(tmpdir.join('test1'))
        dir2 = str(tmpdir.join('test2'))
        makedirs(dir1)
        makedirs(dir2)
        with pytest.raises(Exception) as e:
            copy(dir1, dir2, ignore_errors=False)

    def test_copy_with_ignore_error(self, tmpdir):
        dir1 = str(tmpdir.join('test1'))
        dir2 = str(tmpdir.join('test2'))
        makedirs(dir1)
        makedirs(dir2)
        copy(dir1, dir2, ignore_errors=True)
