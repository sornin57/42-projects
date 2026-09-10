# Python05 - Code Nexus

This module focuses on abstract classes and polymorphism.

## Goal

Build processors that share the same interface but handle different data types.

## Exercises

```text
ex0/data_processor.py   - abstract class and specialized processors
ex1/data_stream.py      - route mixed data with polymorphism
ex2/data_pipeline.py    - export processed data with plugins
```

## Concepts

- `ABC`
- `abstractmethod`
- inheritance
- method overriding
- polymorphism
- protocol
- duck typing

## Useful Commands

Run one exercise:

```bash
python3 ex0/data_processor.py
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

An abstract class is a base model that cannot be used alone.

An abstract method must be rewritten by child classes.

Polymorphism means several objects can be used through the same interface.

A protocol describes what methods an object must have.

Duck typing means Python cares about what an object can do, not only its class.
