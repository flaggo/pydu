import sys
import time
import pytest
from pydu import WINDOWS
from pydu.utils import trace, unix_timeout, TimeoutError
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
