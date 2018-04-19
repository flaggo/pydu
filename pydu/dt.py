import time


class timer(object):
    """
    A timer can time how long does calling take as a context manager or decorator.
    If assign ``print_func`` with ``sys.stdout.write``, ``logger.info`` and so on,
    timer will print the spent time.
    """

    def __init__(self, print_func=None):
        self.elapsed = None
        self.print_func = print_func

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *_):
        self.elapsed = time.time() - self.start
        if self.print_func:
            self.print_func(self.__str__())

    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            with self:
                return fun(*args, **kwargs)
        return wrapper

    def __str__(self):
        return 'Spent time: {}s'.format(self.elapsed)
