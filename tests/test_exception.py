from pydu.exception import ignore


def test_ignore():
    with ignore(ValueError, AttributeError):
        int('abc')
        int.no_exists_func()
