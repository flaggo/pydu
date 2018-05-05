from pydu.slot import SlotBase


class Foo(SlotBase):
    __slots__ = ('a', 'b', 'c')


class TestSlotBase(object):
    def test_args(self):
        foo = Foo(1)
        assert foo.a == 1
        assert foo.b is None
        assert foo.c is None

    def test_kwargs(self):
        foo = Foo(b=2)
        assert foo.a is None
        assert foo.b == 2
        assert foo.c is None

    def test_args_kwargs(self):
        foo = Foo(1, b=2)
        assert foo.a == 1
        assert foo.b == 2
        assert foo.c is None
