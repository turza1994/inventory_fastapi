
# Variables
PYTHON := pipenv run python
UVICORN := pipenv run uvicorn
BLACK := pipenv run black
MYPY := pipenv run mypy
PYLINT := pipenv run pylint

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make install      Install dependencies"
	@echo "  make run          Run the FastAPI development server"
	@echo "  make format       Format code with Black"
	@echo "  make lint         Lint code with Pylint"
	@echo "  make type-check   Run static type checking with Mypy"
	@echo "  make check        Run all checks (format, lint, type-check)"
	@echo "  make clean        Clean up cache files"

.PHONY: install
install:
	pipenv install --dev

.PHONY: run
run:
	$(UVICORN) app.main:app --reload

.PHONY: format
format:
	$(BLACK) app

.PHONY: lint
lint:
	$(PYLINT) app

.PHONY: type-check
type-check:
	$(MYPY) app

.PHONY: check
check: format lint type-check

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
