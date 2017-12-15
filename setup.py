from pydu import __version__
from setuptools import setup, find_packages


setup(
    name="pydu",
    version=__version__,
    description="Useful data structures, utils for Python.",
    long_description=open('README.rst').read(),
    author="Prodesire",
    author_email='wangbinxin001@126.com',
    license='MIT License',
    url="https://github.com/Prodesire/pydu",
    setup_requires=['pytest-runner'],
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
