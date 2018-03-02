# coding: utf-8
import collections


class OrderedSet(object):
    """
    A set which keeps the ordering of the inserted items.
    """

    def __init__(self, iterable=None):
        self.dict = collections.OrderedDict.fromkeys(iterable or ())

    def add(self, item):
        self.dict[item] = None

    def remove(self, item):
        del self.dict[item]

    def discard(self, item):
        try:
            self.remove(item)
        except KeyError:
            pass

    def __iter__(self):
        return iter(self.dict)

    def __contains__(self, item):
        return item in self.dict

    def __bool__(self):
        return bool(self.dict)

    def __nonzero__(self):
        return bool(self.dict)

    def __len__(self):
        return len(self.dict)
