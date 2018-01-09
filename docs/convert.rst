Convert
-------


.. py:function:: pydu.convert.boolean(obj)

    Convert obj to a boolean value.

    If obj is string, obj will converted by case-insensitive way:

        * convert `yes`, `y`, `on`, `true`, `t`, `1` to True
        * convert `no`, `n`, `off`, `false`, `f`, `0` to False
        * raising TypeError if other values passed

    If obj is non-string, obj will converted by ``bool(obj)``.

    >>> from pydu.string import boolean
    >>> boolean('yes')
    True
    >>> boolean('no')
    False
