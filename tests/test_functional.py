from pydu.functional import compose


def test_compose():
    def f1(a, b=1):
        return a+b

    def f2(a):
        return 2*a

    def f3(a, b=3):
        return a+b

    assert compose(f1, f2, f3)(1) == 9
    assert compose(f1, f2, f3)(1, b=5) == 13
