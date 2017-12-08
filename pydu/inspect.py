from __future__ import absolute_import

import inspect

from .compat import PY2


def getargspec(func):
    """
    Get the names and default values of a function's parameters.

    A tuple of four things is returned: (args, varargs, keywords, defaults).
    'args' is a list of the argument names, including keyword-only argument names.
    'varargs' and 'keywords' are the names of the * and ** parameters or None.
    'defaults' is an n-tuple of the default values of the last n parameters.
    """
    if PY2:
        return inspect.getargspec(func)
    else:
        sig = inspect.signature(func)
        args = [
            p.name for p in sig.parameters.values()
            if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        ]
        varargs = [
            p.name for p in sig.parameters.values()
            if p.kind == inspect.Parameter.VAR_POSITIONAL
        ]
        varargs = varargs[0] if varargs else None
        varkw = [
            p.name for p in sig.parameters.values()
            if p.kind == inspect.Parameter.VAR_KEYWORD
        ]
        varkw = varkw[0] if varkw else None
        defaults = [
                       p.default for p in sig.parameters.values()
                       if
                       p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD and p.default is not p.empty
                   ] or None
        return args, varargs, varkw, defaults


def get_func_args(func):
    """
    Return a list of the argument names. Arguments such as
    *args and **kwargs are not included.
    """
    if PY2:
        argspec = inspect.getargspec(func)
        if inspect.ismethod(func):
            return argspec.args[1:] # ignore 'self'
        return argspec.args
    else:
        sig = inspect.signature(func)
        return [
            name for name, param in sig.parameters.items()
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD and name != 'self'
        ]


def get_func_full_args(func):
    """
    Return a list of (argument name, default value) tuples. If the argument
    does not have a default value, omit it in the tuple. Arguments such as
    *args and **kwargs are also included.
    """
    if PY2:
        argspec = inspect.getargspec(func)
        if inspect.ismethod(func):
            args = argspec.args[1:] # ignore 'self'
        else:
            args = argspec.args
        defaults = argspec.defaults or []
        # Split args into two lists depending on whether they have default value
        no_default = args[:len(args) - len(defaults)]
        with_default = args[len(args) - len(defaults):]
        # Join the two lists and combine it with default values
        args = [(arg,) for arg in no_default] + zip(with_default, defaults)
        # Add possible *args and **kwargs and prepend them with '*' or '**'
        varargs = [('*' + argspec.varargs,)] if argspec.varargs else []
        kwargs = [('**' + argspec.keywords,)] if argspec.keywords else []
        return args + varargs + kwargs
    else:
        sig = inspect.signature(func)
        args = []
        for arg_name, param in sig.parameters.items():
            name = arg_name
            # Ignore 'self'
            if name == 'self':
                continue
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                name = '*' + name
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                name = '**' + name
            if param.default != inspect.Parameter.empty:
                args.append((name, param.default))
            else:
                args.append((name,))
        return args


def func_accepts_kwargs(func):
    """
    Check whether or not the func accepts kwargs.
    """
    # Not all callables are inspectable with getargspec, so we'll
    # try a couple different ways but in the end fall back on assuming
    # it is -- we don't want to prevent registration of valid but weird
    # callables.
    if PY2:
        try:
            argspec = inspect.getargspec(func)
        except TypeError:
            try:
                argspec = inspect.getargspec(func.__call__)
            except (TypeError, AttributeError):
                argspec = None
        return not argspec or argspec[2] is not None
    else:
        return any(
            p for p in inspect.signature(func).parameters.values()
            if p.kind == p.VAR_KEYWORD
        )


def func_accepts_var_args(func):
    """
    Check whether or not the func accepts var args.
    """
    if PY2:
        return inspect.getargspec(func)[1] is not None
    else:
        return any(
            p for p in inspect.signature(func).parameters.values()
            if p.kind == p.VAR_POSITIONAL
        )


def func_supports_parameter(func, parameter):
    """
    Check whether or the func supports the given parameter.
    """
    if PY2:
        args, varargs, varkw, defaults = inspect.getargspec(func)
        if inspect.ismethod(func):
            args = args[1:] # ignore 'self'
        return parameter in args + [varargs, varkw]
    else:
        parameters = [name for name in inspect.signature(func).parameters if name != 'self']
        return parameter in parameters


def func_has_no_args(func):
    """
    Check whether or not the func has any args.
    """
    args = inspect.getargspec(func)[0] if PY2 else [
        p for name, p in inspect.signature(func).parameters.items()
        if p.kind == p.POSITIONAL_OR_KEYWORD and name != 'self'
    ]
    return len(args) == 1
