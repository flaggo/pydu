import sys
from pydu.utils import trace
try:
    from cStringIO import StringIO  # py2
except ImportError:
    from io import StringIO  # py3


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
