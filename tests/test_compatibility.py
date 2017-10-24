from pydu.compatibility import (iterkeys, itervalues, iteritems, is_iter,
                                text_type, string_types, numeric_types)


def test_iter():
    d = dict(a=1, b=2)
    for key in iterkeys(d):
        assert key in ('a', 'b')

    for value in itervalues(d):
        assert value in (1, 2)

    for items in iteritems(d):
        assert items in (('a', 1), ('b', 2))

    assert is_iter(iter([]))


def test_types():
    assert isinstance(u'a', text_type)

    assert isinstance(u'a', string_types)
    assert isinstance('a', string_types)

    assert isinstance(1, numeric_types)
    assert isinstance(2**50, numeric_types)


def test_urljoin():
    from pydu.compatibility import urljoin


def test_imap():
    from pydu.compatibility import imap
