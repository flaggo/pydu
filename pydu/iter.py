"""iteration tools"""
from compat import builtins


def first(iterable):
    """
    Get the first item in the iterable.
    """
    return iter(iterable).next()


def last(iterable):
    """
    Get the last item in the iterable.
    Warnning, this can be slow.
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
    return separator.join(map(str, iterable))
