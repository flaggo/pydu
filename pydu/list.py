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
