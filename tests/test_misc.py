import sys
import time
import pytest
from pydu import WINDOWS
from pydu.misc import trace, unix_timeout, TimeoutError, memoize, memoize_when_activated
try:
    from cStringIO import StringIO  # py2
except ImportError:
    from io import StringIO  # py3


@pytest.mark.skipif(WINDOWS, reason='unix_timeout only supports unix-like system')
def test_unix_timeout():
    @unix_timeout(1)
    def f1():
        time.sleep(0.01)

    @unix_timeout(1)
    def f2():
        time.sleep(1.01)

    f1()

    with pytest.raises(TimeoutError):
        f2()


def test_trace():
    @trace
    def f():
        print(1)
        a = 1 + 5
        b = [a]
        print(2)

    old_stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        f()
        sys.stdout.seek(0)
        stdout = sys.stdout.read()
        for statement in ('print(1)',
                          'a = 1 + 5',
                          'b = [a]',
                          'print(2)'):
            assert statement in stdout
    finally:
        sys.stdout = old_stdout


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
        expected = ((1, ), {})
        assert ret == expected
        assert len(calls) == 2

    # with args + kwargs
    for x in range(2):
        ret = foo(1, bar=2)
        expected = ((1, ), {'bar': 2})
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