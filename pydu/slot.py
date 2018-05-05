from .compat import iteritems, izip


class SlotBase(object):
    """
    Base class for class using __slots__.
    If some args or kwargs are not given when initialize class,
    the value of them will be set with ``None``.
    """
    def __init__(self, *args, **kwargs):
        setted = set()
        kwargs_ = dict(izip(self.__slots__, args))
        kwargs_.update(kwargs)
        for key, value in iteritems(kwargs_):
            setattr(self, key, value)
            setted.add(key)
        for key in set(self.__slots__) - setted:
            setattr(self, key, None)
