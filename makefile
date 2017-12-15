# Env
export PYTHONDONTWRITEBYTECODE=1
TEST_PATH=./tests
DEFAULT_PYTHON2=`python -c "import sys;print(sys.version_info.major)" | grep 2`
PY2=$(if $(DEFAULT_PYTHON2),python,python2)
PY3=$(if $(DEFAULT_PYTHON2),python3,python)

# Func
.PHONY: clean-pyc clean-build

help:
	@echo $(PYVER)
	@echo "test"
	@echo "    Run pytest with Python 2 and 3."
	@echo "test-py2"
	@echo "    Run pytest with Python 2."
	@echo "test-py3"
	@echo "    Run pytest with Python 3."
	@echo "clean"
	@echo "    Remove python and build artifacts."
	@echo "clean-pyc"
	@echo "    Remove python artifacts."
	@echo "clean-build"
	@echo "    Remove build artifacts."

test: test-py2 test-py3

test-py2: clean-pyc
	 $(PY2) -m pytest --color=yes $(TEST_PATH)

test-py3: clean-pyc
	 $(PY3) -m pytest --color=yes $(TEST_PATH)

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
