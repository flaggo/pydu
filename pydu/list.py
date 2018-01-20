from collections import Iterable
from pydu.compat import strbytes_types


def uniq(seq, key=None):
    """
    Removes duplicate elements from a list while preserving the order of the rest.

    The value of the optional `key` parameter should be a function that
    takes a single argument and returns a key to test the uniqueness.
    """
    key = key or (lambda x: x)
    seen = set()
    uniq_list = []
    for value in seq:
        uniq_value = key(value)
        if uniq_value in seen:
            continue
        seen.add(uniq_value)
        uniq_list.append(value)
    return uniq_list


def tolist(obj):
    """
    Convert given `obj` to list.

    If `obj` is not a list, return `[obj]`, else return `obj` itself.
    """
    if not isinstance(obj, list):
        return [obj]
    return obj


# https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
def flatten(seq):
    """
    Generate each element of the given `seq`. If the element is iterable and
    is not string, it yields each sub-element of the element recursively.
    """
    for element in seq:
        if isinstance(element, Iterable) and \
                not isinstance(element, strbytes_types):
            for sub in flatten(element):
                yield sub
        else:
            yield element
