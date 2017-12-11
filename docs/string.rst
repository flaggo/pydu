String
------

.. py:function:: pydu.string.safeunicode(obj, encoding='utf-8')

  Converts any given object to unicode string.

    >>> from pydu.string import safeunicode
    >>> safeunicode('hello')
    u'hello'
    >>> safeunicode(2)
    u'2'
    >>> safeunicode('\xe4\xb8\xad\xe6\x96\x87')
    u'中文'


.. py:function:: pydu.string.safeencode(obj, encoding='utf-8')

  Converts any given object to encoded string (default: utf-8).

    >>> from pydu.string import safeencode
    >>> safeencode('hello')
    'hello'
    >>> safeencode(2)
    '2'
    >>> safeencode(u'中文')
    '\xe4\xb8\xad\xe6\x96\x87'


.. py:function:: pydu.string.lstrips(text, remove)

  Removes the string ``remove`` from the left of ``text``.

    >>> from pydu.string import lstrips
    >>> lstrips('foobar', 'foo')
    'bar'
    >>> lstrips('FOOBARBAZ', ['FOO', 'BAR'])
    'BAZ'
    >>> lstrips('FOOBARBAZ', ['BAR', 'FOO'])
    'BARBAZ'


.. py:function:: pydu.string.rstrips(text, remove)

  Removes the string ``remove`` from the right of ``text``.

    >>> from pydu.string import rstrips
    >>> rstrips('foobar', 'bar')
    'foo'


.. py:function:: pydu.string.strips(text, remove)

  Removes the string ``remove`` from the both sides of ``text``.

    >>> from pydu.string import strips
    >>> strips('foobarfoo', 'foo')
    'bar'

.. py:function:: pydu.string.common_prefix(l)

  Return common prefix of the stings

      >>> from pydu.string import common_prefix
      >>> common_prefix(['abcd', 'abc1'])
      'abc'


.. py:function:: pydu.string.common_suffix(l)

  Return common suffix of the stings

      >>> from pydu.string import common_suffix
      >>> common_suffix(['dabc', '1abc'])
      'abc'