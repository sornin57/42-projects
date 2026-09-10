# Python07 - DataDeck

This module focuses on abstract architecture and design patterns.

## Goal

Build card-style creatures with factories, capabilities, and battle strategies.

## Files

```text
battle.py       - tests abstract factories
capacitor.py    - tests creature capabilities
tournament.py   - tests battle strategies
ex0/            - creature factory package
ex1/            - capability package
ex2/            - strategy package
```

## Concepts

- abstract class
- abstract factory
- multiple inheritance
- capability class
- strategy pattern
- package exports with `__init__.py`

## Useful Commands

Run factory test:

```bash
python3 battle.py
```

Run capability test:

```bash
python3 capacitor.py
```

Run tournament test:

```bash
python3 tournament.py
```

Check style:

```bash
flake8 .
```

Check type hints:

```bash
mypy .
```

## Quick Notes

A factory creates objects without exposing the concrete classes.

A capability is a separate behavior, like healing or transforming.

A strategy decides how an object acts during a battle.

The battle code can stay simple because each strategy knows what to do.
