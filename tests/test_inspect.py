from pydu.inspect import (get_func_args, get_func_full_args, func_accepts_var_args,
                          func_accepts_kwargs, func_supports_parameter)


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


def func_no_arguments():
    pass


def func_one_argument(something):
    pass


def func_just_args(*args):
    pass


def func_just_kwargs(**kwargs):
    pass


def func_all_kinds(name, address='home', age=25, *args, **kwargs):
    pass


def test_get_func_args():
    arguments = ['name', 'address', 'age']
    assert get_func_args(Person.all_kinds) == arguments


def test_get_func_full_args():
    # no arguments
    assert get_func_full_args(Person.no_arguments) == []
    assert get_func_full_args(func_no_arguments) == []
    # one argument
    assert get_func_full_args(Person.one_argument) == [('something',)]
    assert get_func_full_args(func_one_argument) == [('something',)]
    # all_arguments
    arguments = [('name',), ('address', 'home'), ('age', 25), ('*args',), ('**kwargs',)]
    assert get_func_full_args(Person.all_kinds) == arguments
    assert get_func_full_args(func_all_kinds) == arguments


def test_func_accepts_var_args():
    # has args
    assert func_accepts_var_args(Person.just_args)
    assert func_accepts_var_args(func_just_args)
    # no args
    assert not func_accepts_var_args(Person.one_argument)
    assert not func_accepts_var_args(func_one_argument)


def test_func_accepts_kwargs():
    # has kwargs
    assert func_accepts_kwargs(Person.just_kwargs)
    assert func_accepts_kwargs(func_just_kwargs)
    # no kwargs
    assert not func_accepts_kwargs(Person.one_argument)
    assert not func_accepts_kwargs(func_one_argument)


def test_func_supports_parameter():
    for all_kinds in Person.all_kinds, func_all_kinds:
        assert func_supports_parameter(all_kinds, 'name')
        assert func_supports_parameter(all_kinds, 'kwargs')
        assert not func_supports_parameter(all_kinds, 'self')