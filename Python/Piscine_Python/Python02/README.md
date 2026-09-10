# Python02 - Garden Guardian

This module focuses on Python exception handling.

## Goal

Build small programs that keep running even when bad data or unexpected problems happen.

## Exercises

```text
ex0/ft_first_exception.py     - convert a temperature and catch invalid input
ex1/ft_raise_exception.py     - raise errors for impossible plant temperatures
ex2/ft_different_errors.py    - handle several built-in error types
ex3/ft_custom_errors.py       - create custom garden exceptions
ex4/ft_finally_block.py       - always clean up with finally
```

## Concepts

- `try`
- `except`
- `raise`
- `finally`
- built-in exceptions
- custom exceptions
- inheritance between exception classes

## Useful Commands

Run one exercise:

```bash
python3 ex0/ft_first_exception.py
```

Run all exercises:

```bash
for file in ex*/*.py; do python3 "$file"; done
```

Check Python syntax:

```bash
python3 -m compileall .
```

Check style:

```bash
flake8 ex*/*.py
```

Check type hints:

```bash
mypy ex*/*.py
```

Note: `ex2` intentionally contains `"Plant age: " + 10` to trigger a
`TypeError`. The subject explains that `mypy` can report this error because
the faulty line is kept on purpose.

Check repository status:

```bash
git status
```

## Quick Notes

`try` contains code that may fail.

`except` catches the error so the program does not crash.

`raise` creates an error manually.

`finally` always runs, even if an error happened.

Custom errors make the code easier to understand because the error name explains
the problem.
