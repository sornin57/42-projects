# Python10 - FuncMage Chronicles

This module focuses on functional programming.

## Goal

Learn how functions can transform data, receive other functions, return functions,
remember values, and wrap behavior.

## Exercises

```text
ex0/lambda_spells.py        - lambda, map, filter, sorted
ex1/higher_magic.py         - functions that receive or return functions
ex2/scope_mysteries.py      - closures and nonlocal
ex3/functools_artifacts.py  - reduce, partial, lru_cache, singledispatch
ex4/decorator_mastery.py    - decorators and staticmethod
```

## Concepts

- lambda
- higher-order function
- closure
- `nonlocal`
- `functools.reduce`
- `functools.partial`
- `functools.lru_cache`
- `functools.singledispatch`
- decorator
- `@staticmethod`

## Useful Commands

Run exercises:

```bash
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

Run all exercises:

```bash
for file in ex*/*.py; do python3 "$file"; done
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

A lambda is a small anonymous function.

A higher-order function receives or returns another function.

A closure is a function that remembers values from where it was created.

`nonlocal` allows an inner function to modify a variable from the outer function.

A decorator wraps a function to add behavior before or after it runs.
