from pydu.utils.dict import attrify


def test_attrify():
    attrd = attrify({
        'a': [1, 2, {'b': 'b'}],
        'c': 'c',
    })
    assert attrd.a == [1, 2, {'b': 'b'}]
    assert attrd.a[2].b == 'b'
    assert attrd.c == 'c'
