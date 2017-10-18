from pydu import __version__
from setuptools import setup, find_packages


setup(
    name="pydu",
    version=__version__,
    description="pydu",
    author="Prodesire",
    url="https://github.com/Prodesire/pydu",
    setup_requires=['pytest-runner'],
    packages=find_packages(),
)
