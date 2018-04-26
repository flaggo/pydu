from pydu.exception import ignore, default_if_except


def test_ignore():
    with ignore(ValueError, AttributeError):
        int('abc')
        int.no_exists_func()


def test_default_if_except():
    @default_if_except(ValueError, default=0)
    def foo():
        return int('abc')

    assert foo() == 0
