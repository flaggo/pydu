v0.7.0 (2018-05-14)
-------------------

**Enhancements**

* Upgrade to **brand new document** powerd by docsify
* Add slot.SlotBase which is the base class for class using `__slots__`
* Add compat.izip


v0.6.2 (2018-04-30)
-------------------

**Enhancements**

* Add ``exception.default_if_except`` which excepts given exceptions and return default value as decorator.


v0.6.1 (2018-04-23)
-------------------

**Enhancements**

* Add ``dt.timer`` which can time how long does calling take as a context manager or decorator.


v0.6.0 (2018-04-16)
-------------------

**Enhancements**

* Add ``path.filename`` which return the filename without extension.
* Add ``path.fileext`` which return the file extension.
* Update stub for ``requests.check_connect``.


v0.5.2 (2018-04-04)
-------------------

**Enhancements**

* Add ``system.preferredencoding`` which gets best encoding for the system.
* Add ``request.update_query_params`` which update query params of given url and return new url.
* Update stub for ``requests.check_connect``.


v0.5.1 (2018-03-19)
-------------------

**Enhancements**

* Improve ``system.remove`` when path is read-only.
* Add ``path.normjoin`` which join one or more path components intelligently and normalize it.
* Improve ``environ.environ`` with supporting variable_name=None which means removing the variable from environment temporarily.


v0.5.0 (2018-03-08)
-------------------

**Enhancements**

* Add ``network.private_ipv4s`` which stores private IPV4 addresses.
* Add ``functional.compose`` which composes all functions into one.
* Add ``TYPE HINT`` for ALL MODULES by supplying STUB FILES!

**Bug fixes**

* Fix reduce error on Python 3.


v0.4.2 (2018-02-05)
-------------------

**Enhancements**

* Add ``socket.inet_pton`` and ``socket.inetntop`` for Windows if we ``import pydu.network``.
* Add ``network.ip2int`` and ``network.int2ip`` which convert ip to integer or integer to ip.
* Add ``process.get_processes_by_path`` for getting processes which are running on given path or sub path of given path.
* Add ``first``, ``last``, ``all``, ``any`` and ``join`` to ``pydu.iter``, which support many operations on iterable object.

**Bug fixes**

* Fix several convert functions return values with unnecessary value 'L' when given big number on Python 2.


v0.4.1 (2018-01-20)
-------------------

**Enhancements**

* Add ``bin2oct``, ``bin2dec``, ``bin2hex``, ``oct2bin``, ``oct2dec``, ``oct2hex``, ``dec2bin``, ``dec2oct``, ``dec2hex``, ``hex2bin``, ``hex2oct``, ``hex2dec`` to ``convert``, which support many base conversions
* Add ``path.is_super_path`` which judges whether the given ``path1`` is the super path of ``path2``
* Add ``environ.environ`` which is a context manager for updating one or more environment variables
* Add ``environ.path`` which is a context manager for updating the PATH environment variable
* Add ``list.tolist`` which converts obj to list
* Add ``list.flatten`` which generates each element of the given ``seq``
* Add ``compat.strbytes_types`` which includes all types about string


v0.4.0 (2018-01-09)
-------------------

**Importance**
* Remove support for Python 3.4

**Enhancements**

* Add ``dict.OrderedDefaultDict`` which remembers insertion order and has default value with default factory
* Add ``convert.boolean`` which converts obj to a boolean value
* ``console.console_size`` will use ``shutil.get_terminal_size`` if possible
* ``exception.ignore`` is same to ``context.lib.suppress`` on Python 3

**Bug fixes**

* Fix #15 (If the ``dict.attrify``'s obj is tuple, this will raise a error)


v0.3.1 (2017-12-29)
-------------------

**Enhancements**

* Add ``FileTracker`` which could track opening files.


**Bug fixes**

* Fix ``pip install`` error on Windows with Python 3.
* Fix ``network.is_ipv6`` test error on Windows with Python 3.
* Fix description error on ``network``, ``request`` doc.


v0.3.0 (2017-12-26)
-------------------

**Enhancements**

* Rename ``file`` to ``system``.
* Add ``system.which`` which supports find executable file.
* Add ``system.chmod`` which supports chmod recursively.
* Add ``unit.Bytes`` which used to deal with bytes.
* Add ``preferredencoding`` to ``string``.
* Add ``cmd.chcp`` for Windows which is same like ``chcp`` on Windows cmd.
* Add ``cmd.run_with_en_env`` which ensure the output of cmd is in English.
* Add ``cmd.terminate`` which supports terminate process by given ``pid``.
* ``cmd.run`` uses timeout feature on Python 3 but not implement by self.


**Bug fixes**

* Fix test cases to generate right coverage.


v0.2.0 (2017-12-17)
-------------------

**Enhancements**

* Add ``exception.ignore``.
* ``network.is_ipv6`` is available on Windows.
* Set logging handler to avoid "No handler found" warnings.
* Add ``Makefile`` which make development easier.
* Update ``readme`` which is more readable.

**Bug fixes**

* Fix installation error on Windows.


v0.1.0 (2017-12-14)
-------------------

Supply many powerful data structures and utils about archive, cmd, compat, console, dict, file, inspect, list, misc, network, path, platform, request, set and string.