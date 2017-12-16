# Env
export PYTHONDONTWRITEBYTECODE=1
TEST_PATH=./tests
DEFAULT_PYTHON2=`python -c "import sys;print(sys.version_info.major)" | grep 2`
PY2=$(if $(DEFAULT_PYTHON2),python,python2)
PY3=$(if $(DEFAULT_PYTHON2),python3,python)

# Func
.PHONY: docs

help:
	@echo "init"
	@echo "    Init environment for pydu."
	@echo "test"
	@echo "    Run pytest with Python 2 and 3."
	@echo "test-py2"
	@echo "    Run pytest with Python 2."
	@echo "test-py3"
	@echo "    Run pytest with Python 3."
	@echo "coverage"
	@echo "    Run pytest and report coverage."
	@echo "docs"
	@echo "    Make docs for pydu."
	@echo "clean"
	@echo "    Remove python and build artifacts."
	@echo "clean-pyc"
	@echo "    Remove python artifacts."
	@echo "clean-build"
	@echo "    Remove build artifacts."

init:
	pip install -r requirements-dev.txt

test: test-py2 test-py3

test-py2: clean-pyc
	 $(PY2) -m pytest --color=yes $(TEST_PATH)

test-py3: clean-pyc
	 $(PY3) -m pytest --color=yes $(TEST_PATH)

coverage:
	coverage run --source=pydu -m pytest tests
	coverage report

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

clean: clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
