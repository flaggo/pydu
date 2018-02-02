"""iteration tools"""


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
