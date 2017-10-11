from pydu.utils import attrify


def test_attrify():
    attrd = attrify({
        'a': [1, 2, {'b': 'b'}],
        'c': 'c',
    })
    print(attrd)
    assert attrd.a == [1, 2, {'b': 'b'}]
    assert attrd.a[2].b == 'b'
    assert attrd.c == 'c'
