import os
from pydu.dt import timer


class TestTimer(object):
    def test_context_manager(self):
        timeit = timer()

        with timeit:
            os.getcwd()

        assert timeit.elapsed is not None

    def test_decorator(self):
        import sys
        timeit = timer(print_func=print)

        @timeit
        def foo():
            os.getcwd()

        foo()
        assert timeit.elapsed is not None
