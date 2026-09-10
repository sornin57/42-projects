# Python08 - The Matrix

This module focuses on environments, packages, and configuration.

## Goal

Understand how to isolate a Python project, install dependencies, and keep
configuration outside the code.

## Exercises

```text
ex0/construct.py   - detect if Python runs inside a virtual environment
ex1/loading.py     - use pandas, numpy, matplotlib, pip, and Poetry
ex2/oracle.py      - load configuration from environment variables
```

## Concepts

- virtual environment
- `sys.executable`
- `sys.prefix`
- `requirements.txt`
- `pyproject.toml`
- dependency check
- `.env`
- `.env.example`
- `.gitignore`

## Useful Commands

Create a virtual environment:

```bash
python3 -m venv matrix_env
```

Activate it:

```bash
source matrix_env/bin/activate
```

Install dependencies with pip:

```bash
pip install -r ex1/requirements.txt
pip install -r ex2/requirements.txt
```

Install dependencies with Poetry:

```bash
cd ex1
poetry install
```

Create a local environment file:

```bash
cd ex2
cp .env.example .env
```

Run the exercises:

```bash
python3 ex0/construct.py
python3 ex1/loading.py
python3 ex2/oracle.py
```

Check style:

```bash
flake8 ex*/*.py
```

Check type hints:

```bash
mypy ex*/*.py
```

## Quick Notes

A virtual environment isolates dependencies from the global Python installation.

`requirements.txt` is commonly used with pip.

`pyproject.toml` is commonly used by modern Python tools such as Poetry.

Secrets should stay in `.env`, never directly in the code.

`.env.example` shows the expected variables without real secrets.
