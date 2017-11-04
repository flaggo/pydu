from pydu.inspect import (get_func_full_args, func_accepts_var_args,
                          func_accepts_kwargs)


class Person:
    def no_arguments(self):
        return None

    def one_argument(self, something):
        return something

    def just_args(self, *args):
        return args

    def just_kwargs(self, **kwargs):
        return kwargs

    def all_kinds(self, name, address='home', age=25, *args, **kwargs):
        return kwargs


def test_get_func_full_args():
    # no arguments
    assert get_func_full_args(Person.no_arguments) == []
    # one argument
    assert get_func_full_args(Person.one_argument) == [('something',)]
    # all_arguments
    arguments = [('name',), ('address', 'home'), ('age', 25), ('*args',), ('**kwargs',)]
    assert get_func_full_args(Person.all_kinds) == arguments


def test_func_accepts_var_args():
    # has args
    assert func_accepts_var_args(Person.just_args)
    # no args
    assert not func_accepts_var_args(Person.one_argument)


def test_func_accepts_kwargs():
    # has kwargs
    assert func_accepts_kwargs(Person.just_kwargs)
    # no kwargs
    assert not func_accepts_kwargs(Person.one_argument)
