from pylib.utils import strips, lstrips, rstrips


def test_lstrips():
    assert lstrips('foobbar', '') == 'foobbar'
    assert lstrips('foobar', 'fo') == 'obar'
    assert lstrips('foofoobar', 'foo') == 'foobar'
    assert lstrips('foobarbaz', ('foo', 'bar')) == 'baz'
    assert lstrips('foobarbaz', ('bar', 'foo')) == 'barbaz'


def test_rstrips():
    assert rstrips('foobbar', '') == 'foobbar'
    assert rstrips('foobbar', 'bar') == 'foob'
    assert rstrips('foobarbar', 'bar') == 'foobar'
    assert rstrips('fozfoobar', ('bar', 'foo')) == 'foz'
    assert rstrips('fozfoobar', ('foo', 'bar')) == 'fozfoo'


def test_strips():
    assert strips('foobarfoo', '') == 'foobarfoo'
    assert strips('foobarfoo', 'foo') == 'bar'
    assert strips('foobarfoo', ('foo', 'bar')) == ''
