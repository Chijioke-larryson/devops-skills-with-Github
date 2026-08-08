.PHONY: all install check-python test format limit refactor

# Prefer python3 on macOS, fall back to python when available.
PYTHON ?= $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)
PIP := $(PYTHON) -m pip

check-python:
	@if [ -z "$(PYTHON)" ]; then \
		echo "Python 3 is required but was not found in PATH."; \
		echo "Install Python, then rerun: make install && make test"; \
		exit 1; \
	fi

install:
	@echo "Installing dependencies..."
	@$(MAKE) check-python
	$(PIP) install -r requirements.txt

all: test format limit refactor

test:
	@echo "Running tests..."
	@$(MAKE) check-python
	$(PYTHON) -m pytest -vv test_*.py --disable-warnings --maxfail=1 --cov=hello

format:
	@echo "Formatting code..."
	black .
	isort .

limit:
	@echo "Checking linting and limits..."
	# check style and enforce max line length
	flake8 --max-line-length=88 .

refactor:
	@echo "Refactoring / cleaning imports..."
	# remove unused imports/vars and try automated fixes
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r . || true
	ruff fix . || true
