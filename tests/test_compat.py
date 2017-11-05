from pydu.compat import (PY2, iterkeys, itervalues, iteritems,
                         text_type, string_types, numeric_types,
                         is_iterable, has_next_attr)


def test_itersth():
    d = dict(a=1, b=2)
    for key in iterkeys(d):
        assert key in ('a', 'b')

    for value in itervalues(d):
        assert value in (1, 2)

    for items in iteritems(d):
        assert items in (('a', 1), ('b', 2))


def test_has_next_attr():
    if PY2:
        class NextAttr:
            def next(self):
                pass
    else:
        class NextAttr:
            def __next__(self):
                pass
    assert has_next_attr(NextAttr())
    assert not has_next_attr('')


def test_is_iterable():
    assert is_iterable(list())
    assert is_iterable(tuple())
    assert is_iterable(dict())
    assert is_iterable(set())
    assert not is_iterable(1)


def test_types():
    assert isinstance(u'a', text_type)

    assert isinstance(u'a', string_types)
    assert isinstance('a', string_types)

    assert isinstance(1, numeric_types)
    assert isinstance(2**50, numeric_types)


def test_urljoin():
    from pydu.compat import urljoin


def test_imap():
    from pydu.compat import imap