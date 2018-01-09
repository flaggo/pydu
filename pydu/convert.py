

def boolean(obj):
    """
    Convert obj to a boolean value.
    If obj is string, obj will converted by case-insensitive way:
        * convert `yes`, `y`, `on`, `true`, `t`, `1` to True
        * convert `no`, `n`, `off`, `false`, `f`, `0` to False
        * raising TypeError if other values passed
    If obj is non-string, obj will converted by bool(obj).
    """

    try:
        text = obj.strip().lower()
    except AttributeError:
        return bool(obj)

    if text in ('yes', 'y', 'on', 'true', 't', '1'):
        return True
    elif text in ('no', 'n', 'off', 'false', 'f', '0'):
        return False
    else:
        raise ValueError("Unable to convert {!r} to a boolean value.".format(text))
