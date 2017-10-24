from pydu.datastructures.dict import AttrDict


def attrify(obj):
    if isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            obj[i] = attrify(v)
        return obj
    elif isinstance(obj, dict):
        attrd = AttrDict()
        for key, value in obj.items():
            value = attrify(value)
            setattr(attrd, key, value)
        return attrd
    else:
        return obj
