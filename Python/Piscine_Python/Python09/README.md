# Python09 - Cosmic Data

This module focuses on Pydantic models and validation.

## Goal

Use Pydantic to validate structured data before using it in a program.

## Exercises

```text
ex0/space_station.py   - basic model with Field validation
ex1/alien_contact.py   - custom validation with model_validator
ex2/space_crew.py      - nested models and mission validation
```

## Concepts

- `BaseModel`
- `Field`
- `Enum`
- `ValidationError`
- `model_validator`
- nested models
- optional fields
- default values

## Useful Commands

Install Pydantic:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or directly:

```bash
pip install "pydantic>=2"
```

Run exercises:

```bash
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
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

Pydantic checks the type and value of data when an object is created.

`Field` adds rules such as minimum length or maximum value.

`model_validator` checks rules that need several fields at the same time.

Nested models allow one model to contain other validated models.
