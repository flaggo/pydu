# Env
export PYTHONDONTWRITEBYTECODE=1
TEST_PATH=./tests
UV_PYTHON_FLAG=$(if $(PY),--python $(PY),)

# Func
.PHONY: help install init test coverage build check publish docs clean clean-pyc clean-build

help:
	@echo "\033[32minstall\033[0m"
	@echo "    Install dependencies with uv."
	@echo "\033[32minit\033[0m"
	@echo "    Init environment for pydu."
	@echo "\033[32mtest\033[0m"
	@echo "    Run pytest."
	@echo "\033[32mcoverage\033[0m"
	@echo "    Run pytest and report coverage."
	@echo "\033[32mbuild\033[0m"
	@echo "    Build distributions."
	@echo "\033[32mcheck\033[0m"
	@echo "    Check built distributions."
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

install:
	uv sync $(UV_PYTHON_FLAG) --group dev

init:
	$(MAKE) install
	npm i docsify-cli -g

test: clean-pyc
	uv run $(UV_PYTHON_FLAG) pytest --color=yes $(TEST_PATH)

coverage:
	uv run $(UV_PYTHON_FLAG) coverage run --source=pydu -m pytest tests
	uv run $(UV_PYTHON_FLAG) coverage report

build: clean-build
	uv build $(UV_PYTHON_FLAG)

check:
	uv run $(UV_PYTHON_FLAG) twine check dist/*

publish:
	uv publish

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
