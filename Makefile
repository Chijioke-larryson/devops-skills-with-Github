.PHONY: all test format limit refactor
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

all: test format limit refactor

test:
	@echo "Running tests..."
	pytest -q

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
