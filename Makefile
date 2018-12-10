# Env
export PYTHONDONTWRITEBYTECODE=1
TEST_PATH=./tests
DEFAULT_PYTHON2=`python -c "import sys;print(sys.version_info.major)" | grep 2`
PY2=$(if $(DEFAULT_PYTHON2),python,python2)
PY3=$(if $(DEFAULT_PYTHON2),python3,python)

# Func
.PHONY: docs

help:
	@echo "\033[32minit\033[0m"
	@echo "    Init environment for pydu."
	@echo "\033[32mtest\033[0m"
	@echo "    Run pytest with Python 2 and 3."
	@echo "\033[32mtest-py2\033[0m"
	@echo "    Run pytest with Python 2."
	@echo "\033[32mtest-py3\033[0m"
	@echo "    Run pytest with Python 3."
	@echo "\033[32mcoverage\033[0m"
	@echo "    Run pytest and report coverage."
	@echo "\033[32mpublish\033[0m"
	@echo "    Publish pydu to PyPI."
	@echo "\033[32mdocs\033[0m"
	@echo "    Make docs for pydu."
	@echo "\033[32mclean\033[0m"
	@echo "    Remove python and build artifacts."
	@echo "\033[32mclean-pyc\033[0m"
	@echo "    Remove python artifacts."
	@echo "\033[32mclean-build\033[0m"
	@echo "    Remove build artifacts."

init:
	pip install -r requirements-dev.txt
	npm i docsify-cli -g

test: test-py2 test-py3

test-py2: clean-pyc
	 $(PY2) -m pytest --color=yes $(TEST_PATH)

test-py3: clean-pyc
	 $(PY3) -m pytest --color=yes $(TEST_PATH)

coverage:
	coverage run --source=pydu -m pytest tests
	coverage report

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist
	twine upload dist/*
	rm -rf build dist *.egg-info .eggs

docs:
	docsify serve docs

clean: clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-build:
	rm -rf build dist *.egg-info .eggs
