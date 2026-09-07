PYTHON = python3
VENV = .venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV)/bin/pip
MAP ?= maps/easy/01_linear_path.txt

.PHONY: help install run debug clean lint test check


help:
	@echo "Fly-in Makefile commands:"
	@echo "  make install  - Create .venv and install flake8 and mypy"
	@echo "  make run      - Run the default map"
	@echo "  make run MAP=path/to/map.txt - Run a specific map"
	@echo "  make debug    - Run the program with pdb"
	@echo "  make lint     - Run flake8 and strict mypy checks"
	@echo "  make test     - Run the unit tests"
	@echo "  make check    - Run lint and tests"
	@echo "  make clean    - Remove Python and macOS cache files"
	@echo ""
	@echo "Virtual environment commands:"
	@echo "  source .venv/bin/activate - Activate the environment"
	@echo "  deactivate                - Leave the environment"

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install flake8 mypy

run:
	$(PYTHON) main.py $(MAP)

debug:
	$(PYTHON) -m pdb main.py $(MAP)

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

lint:
	$(VENV_PYTHON) -m flake8 . --exclude=.venv
	$(VENV_PYTHON) -m mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

test:
	$(PYTHON) -m unittest discover -s tests

check: lint test
