import sys
from pydu import __version__
from pydu.compat import PY2
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count
            self.pytest_args = ['-n', str(cpu_count())]
        except (ImportError, NotImplementedError):
            self.pytest_args = ['-n', '1']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


test_requirements = []
for line in open('requirements-dev.txt'):
    requirement = line.strip()
    if requirement:
        test_requirements.append(requirement)


open_kwargs = {} if PY2 else {'encoding': 'utf-8'}
setup(
    name="pydu",
    version=__version__,
    description="Useful data structures, utils for Python.",
    long_description=open('README.rst', **open_kwargs).read(),
    author="Prodesire",
    author_email='wangbinxin001@126.com',
    license='MIT License',
    url="https://github.com/Prodesire/pydu",
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
