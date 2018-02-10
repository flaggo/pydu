from .compat import reduce


def compose(*funcs):
    """
    Compose all functions. The previous function must accept one argument,
    which is the output of the next function. The last function can accept
    any args and kwargs.

    compose(f1, f2, f3)(*x) is same to f1(f2(f3(*x))).
    """
    return reduce(
        lambda f1, f2: (lambda *args, **kwargs: f2(f1(*args, **kwargs))),
        reversed(funcs))
