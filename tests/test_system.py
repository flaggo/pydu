import os
import stat
import time
import tempfile

import pytest

from pydu.platform import WINDOWS
from pydu.system import makedirs, remove, removes, open_file, copy, touch, which

if not WINDOWS:
    from pydu.system import link, symlink, chmod


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


class TestRemove:
    def test_remove_dir(self, tmpdir):
        path = str(tmpdir.join('test'))
        makedirs(path)
        remove(path)
        assert not os.path.exists(path)

    def test_remove_file(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        touch(f)
        remove(f)
        assert not os.path.exists(f)

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
        with pytest.raises(Exception):
            remove(path, ignore_errors=False)

    def test_remove_without_ignore_error_with_onerror(self):
        pass


class TestRemoves:
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

    def test_removes_files(self, tmpdir):
        f1 = str(tmpdir.join('test1.txt'))
        f2 = str(tmpdir.join('test2.txt'))
        f3 = str(tmpdir.join('test3.txt'))
        for f in [f1, f2, f3]:
            touch(f)
        removes([f1, f2, f3])
        for f in [f1, f2, f3]:
            assert not os.path.exists(f)

    def test_removes_files_and_path(self, tmpdir):
        f1 = str(tmpdir.join('test1.txt'))
        f2 = str(tmpdir.join('test2.txt'))
        p1 = str(tmpdir.join('test1'))
        p2 = str(tmpdir.join('test2'))
        for f in [f1, f2]:
            touch(f)
        for p in [p1, p2]:
            makedirs(p)
        removes([f1, f2, p1, p2])
        for f in [f1, f2, p1, p2]:
            assert not os.path.exists(f)


class TestOpenFile:
    def test_open_file_without_parent_dir(self, tmpdir):
        f = str(tmpdir.join('test/test1.txt'))
        open_file(f)
        assert os.path.exists(f)

    def test_open_file_in_exist_path(self, tmpdir):
        f = str(tmpdir.join('test2.txt'))
        open_file(f)
        assert os.path.exists(f)

    def test_open_exist_file(self, tmpdir):
        f = str(tmpdir.join('test3.txt'))
        open_file(f)
        with open(f, 'r') as f:
            with pytest.raises(Exception):
                os.remove(f)

    def test_open_file_with_ignore_error(self, tmpdir):
        f = str(tmpdir.join('test1.txt'))
        open_file(f, mode='r', ignore_errors=True)

    def test_open_file_without_ignore_error(self, tmpdir):
        f = str(tmpdir.join('test1.txt'))
        with pytest.raises(Exception):
            open_file(f, mode='r')


@pytest.mark.skipif(WINDOWS, reason='Not support on windows')
class TestLink:
    def test_link_a_file(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        touch(f)
        link(f, link_f)
        assert os.path.exists(link_f)

    def test_link_with_ignore_error(self, tmpdir):
        dirname = str(tmpdir.join('test'))
        link_dirname = str(tmpdir.join('test.link'))
        makedirs(dirname)
        link(dirname, link_dirname, ignore_errors=True)

    def test_link_without_ignore_error(self, tmpdir):
        d = str(tmpdir.join('test'))
        link_d = str(tmpdir.join('test.link'))
        makedirs(d)
        with pytest.raises(Exception):
            link(d, link_d)

    def test_link_with_overwrite(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        touch(f)
        link(f, link_f)
        t1 = os.path.getctime(link_f)
        time.sleep(0.1)
        link(f, link_f, overwrite=True)
        t2 = os.path.getctime(link_f)
        assert t1 != t2


@pytest.mark.skipif(WINDOWS, reason='Not support on windows')
class TestSymLink:
    def test_symlink_a_file(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        touch(f)
        symlink(f, link_f)
        assert os.path.exists(link_f)
        assert os.path.islink(link_f)

    def test_symlink_with_ignore_error(self, tmpdir):
        d = str(tmpdir.join('test'))
        link_d = str(tmpdir.join('test.link'))
        makedirs(d)
        link(d, link_d, ignore_errors=True)

    def test_symlink_with_overwrite(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        touch(f)
        symlink(f, link_f)
        t1 = os.lstat(link_f).st_ctime
        time.sleep(0.01)
        symlink(f, link_f, overwrite=True)
        t2 = os.lstat(link_f).st_ctime
        assert t1 != t2

    def test_symlink_without_ignore_error(self, tmpdir):
        d = str(tmpdir.join('test'))
        link_d = str(tmpdir.join('test.link'))
        makedirs(d)
        with pytest.raises(Exception):
            link(d, link_d)


class TestCopy:
    def test_copy_file(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        f_copy = str(tmpdir.join('test_copy.txt'))
        touch(f)
        copy(f, f_copy)
        assert os.path.exists(f_copy)

    def test_copy_non_empty_dir(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        d_copy = str(tmpdir.join('test_copy'))
        os.makedirs(d)
        touch(f)
        copy(d, d_copy)
        assert os.path.exists(d_copy)

    def test_copy_empty_dir(self, tmpdir):
        d = str(tmpdir.join('test'))
        d_copy = str(tmpdir.join('test_copy'))
        makedirs(d)
        copy(d, d_copy)
        assert os.path.exists(d_copy)

    @pytest.mark.skipif(WINDOWS, reason='Not support on windows')
    def test_copy_dir_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        link_f = str(tmpdir.join('test/test_link.txt'))
        d_copy = str(tmpdir.join('test_copy'))
        new_link_f = str(tmpdir.join('test_copy/test_link.txt'))
        makedirs(d)
        touch(f)
        os.symlink(f, link_f)
        copy(d, d_copy, follow_symlinks=True)
        assert os.path.exists(d_copy)
        assert os.path.islink(new_link_f)

    @pytest.mark.skipif(WINDOWS, reason='Not support on windows')
    def test_copy_dir_not_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test/test.txt'))
        d = str(tmpdir.join('test'))
        link_f = str(tmpdir.join('test/test_link.txt'))
        d_copy = str(tmpdir.join('test_copy'))
        new_link_f = str(tmpdir.join('test_copy/test_link.txt'))
        makedirs(d)
        touch(f)
        os.symlink(f, link_f)
        copy(d, d_copy, follow_symlinks=False)
        assert os.path.exists(d_copy)
        assert not os.path.islink(new_link_f)

    @pytest.mark.skipif(WINDOWS, reason='Not support on windows')
    def test_copy_file_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        copy_link_f = str(tmpdir.join('test_copy.link'))
        touch(f)
        link(f, link_f)
        copy(link_f, copy_link_f, follow_symlinks=True)
        assert os.path.exists(copy_link_f)
        assert not os.path.islink(copy_link_f)

    @pytest.mark.skipif(WINDOWS, reason='Not support on windows')
    def test_copy_file_not_follow_symlink(self, tmpdir):
        f = str(tmpdir.join('test.txt'))
        link_f = str(tmpdir.join('test.link'))
        copy_link_f = str(tmpdir.join('test_copy.link'))
        touch(f)
        os.symlink(f, link_f)
        copy(link_f, copy_link_f, follow_symlinks=False)
        assert os.path.exists(copy_link_f)
        assert os.path.islink(copy_link_f)

    def test_copy_path_to_exits_path(self, tmpdir):
        d1 = str(tmpdir.join('test1'))
        d2 = str(tmpdir.join('test2'))
        makedirs(d1)
        makedirs(d2)
        with pytest.raises(Exception):
            copy(d1, d2)

    def test_copy_without_ignore_error(self, tmpdir):
        d1 = str(tmpdir.join('test1'))
        d2 = str(tmpdir.join('test2'))
        makedirs(d1)
        makedirs(d2)
        with pytest.raises(Exception):
            copy(d1, d2, ignore_errors=False)

    def test_copy_with_ignore_error(self, tmpdir):
        d1 = str(tmpdir.join('test1'))
        d2 = str(tmpdir.join('test2'))
        makedirs(d1)
        makedirs(d2)
        copy(d1, d2, ignore_errors=True)


@pytest.fixture()
def mycmd(tmpdir):
    mycmd = str(tmpdir.join('mycmd'))
    touch(mycmd)
    os.chmod(mycmd, os.F_OK | stat.S_IXUSR)
    os.environ['PATHEXT'] = ''
    return mycmd


@pytest.mark.usefixtures('mycmd')
class TestWhich:
    def test_dir_cmd(self, mycmd):
        assert which('noexists/mycmd') is None
        assert which(mycmd) == mycmd

    def test_cmd_path(self, tmpdir, mycmd):
        path = str(tmpdir)
        assert which('mycmd') is None
        assert which('mycmd', path=path) == mycmd

        os.environ['PATH'] = path + os.pathsep + \
                             os.environ.get('PATH', os.defpath)
        assert which('mycmd') == mycmd


@pytest.mark.skipif(not WINDOWS, reason='Not support non Windows')
def test_chcp():
    from pydu.system import chcp
    from ctypes import windll

    origin_code = windll.kernel32.GetConsoleOutputCP()
    with chcp(437):
        assert windll.kernel32.GetConsoleOutputCP() == 437
    assert windll.kernel32.GetConsoleOutputCP() == origin_code

    try:
        cp = chcp(437)
        assert windll.kernel32.GetConsoleOutputCP() == 437
        assert str(cp) == '<active code page number: 437>'
    finally:
        windll.kernel32.SetConsoleOutputCP(origin_code)


class TestChmod:
    def test_chmod_file(self):
        _, t_file = tempfile.mkstemp()
        chmod(t_file, 0o666)
        assert oct(os.stat(t_file).st_mode)[-3:] == '666'

    def test_chmod_dir(self):
        t_dir = tempfile.mkdtemp()
        for _ in range(5):
            tempfile.mkstemp(dir=t_dir)
        chmod(t_dir, 0o666, True)
        for root, _, files in os.walk(t_dir):
            assert oct(os.stat(root).st_mode)[-3:] == '666'
            for file_ in files:
                assert oct(os.stat(os.path.join(root, file_)).st_mode)[-3:] == '666'

