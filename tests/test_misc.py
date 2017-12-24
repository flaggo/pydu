import sys
import time
import pytest
from pydu.misc import (trace, TimeoutError, timeout,
                       memoize, memoize_when_activated,
                       super_len)

try:
    from cStringIO import StringIO  # py2
except ImportError:
    from io import StringIO  # py3


def test_timeout():
    @timeout(1)
    def f1():
        time.sleep(0.01)
        return 1

    @timeout(0.01)
    def f2():
        time.sleep(1)
        return 2

    assert f1() == 1
    with pytest.raises(TimeoutError):
        f2()


def test_memoize():
    @memoize
    def foo(*args, **kwargs):
        """foo docstring"""
        calls.append(None)
        return (args, kwargs)

    calls = []
    # no args
    for x in range(2):
        ret = foo()
        expected = ((), {})
        assert ret == expected
        assert len(calls) == 1

    # with args
    for x in range(2):
        ret = foo(1)
        expected = ((1,), {})
        assert ret == expected
        assert len(calls) == 2

    # with args + kwargs
    for x in range(2):
        ret = foo(1, bar=2)
        expected = ((1,), {'bar': 2})
        assert ret == expected
        assert len(calls) == 3

    # clear cache
    foo.cache_clear()
    ret = foo()
    expected = ((), {})
    assert ret == expected
    assert len(calls) == 4

    # docstring
    assert foo.__doc__ == "foo docstring"


def test_memoize_when_activated():
    class Foo:
        @memoize_when_activated
        def foo(self):
            calls.append(None)

    f = Foo()
    calls = []
    f.foo()
    f.foo()
    assert len(calls) == 2

    # activate
    calls = []
    f.foo.cache_activate()
    f.foo()
    f.foo()
    assert len(calls) == 1

    # deactivate
    calls = []
    f.foo.cache_deactivate()
    f.foo()
    f.foo()
    assert len(calls) == 2


class TestSuperLen:
    @pytest.mark.parametrize(
        'stream, value', (
            (StringIO, 'Test'),
        ))
    def test_io_streams(self, stream, value):
        """Ensures that we properly deal with different kinds of IO streams."""
        assert super_len(stream()) == 0
        assert super_len(stream(value)) == 4

    def test_super_len_correctly_calculates_len_of_partially_read_file(self):
        """Ensure that we handle partially consumed file like objects."""
        s = StringIO()
        s.write('foobarbogus')
        assert super_len(s) == 0

    @pytest.mark.parametrize('error', [IOError, OSError])
    def test_super_len_handles_files_raising_weird_errors_in_tell(self, error):
        """If tell() raises errors, assume the cursor is at position zero."""

        class BoomFile(object):
            def __len__(self):
                return 5

            def tell(self):
                raise error()

        assert super_len(BoomFile()) == 0

    @pytest.mark.parametrize('error', [IOError, OSError])
    def test_super_len_tell_ioerror(self, error):
        """Ensure that if tell gives an IOError super_len doesn't fail"""

        class NoLenBoomFile(object):
            def tell(self):
                raise error()

            def seek(self, offset, whence):
                pass

        assert super_len(NoLenBoomFile()) == 0

    def test_string(self):
        assert super_len('Test') == 4

    @pytest.mark.parametrize(
        'mode, warnings_num', (
            ('r', 0),
            ('rb', 0),
        ))
    def test_file(self, tmpdir, mode, warnings_num, recwarn):
        file_obj = tmpdir.join('test.txt')
        file_obj.write('Test')
        with file_obj.open(mode) as fd:
            assert super_len(fd) == 4
        assert len(recwarn) == warnings_num

    def test_super_len_with__len__(self):
        foo = [1, 2, 3, 4]
        len_foo = super_len(foo)
        assert len_foo == 4

    def test_super_len_with_no__len__(self):
        class LenFile(object):
            def __init__(self):
                self.len = 5

        assert super_len(LenFile()) == 5

    def test_super_len_with_tell(self):
        foo = StringIO('12345')
        assert super_len(foo) == 5
        foo.read(2)
        assert super_len(foo) == 3

    def test_super_len_with_fileno(self):
        with open(__file__, 'rb') as f:
            length = super_len(f)
            file_data = f.read()
        assert length == len(file_data)

    def test_super_len_with_no_matches(self):
        """Ensure that objects without any length methods default to 0"""
        assert super_len(object()) == 0
