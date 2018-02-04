"""iteration tools"""
from .compat import builtins, imap


def first(iterable):
    """
    Get the first item in the iterable.
    """
    return next(iter(iterable))


def last(iterable):
    """
    Get the last item in the iterable.
    Warning, this can be slow due to iter step by step to last one.
    """
    item = None
    for item in iterable:
        pass
    return item


def all(iterable, predicate):
    """
    Returns True if all elements in the given iterable are True for the
    given predicate function.
    """
    return builtins.all(predicate(x) for x in iterable)


def any(iterable, predicate):
    """
    Returns True if any element in the given iterable is True for the
    given predicate function.
    """
    return builtins.any(predicate(x) for x in iterable)


def join(iterable, separator=''):
    """
    Join each item of iterable to string.
    """
    return separator.join(imap(str, iterable))
