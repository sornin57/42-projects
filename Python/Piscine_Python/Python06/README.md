# Python06 - Import Mysteries

This module focuses on Python imports and packages.

## Goal

Understand how files can import each other and how a folder becomes a package.

## Structure

```text
alchemy/
├── __init__.py
├── elements.py
├── grimoire/
├── potions.py
└── transmutation/
```

## Concepts

- local imports
- package imports
- `__init__.py`
- absolute imports
- relative imports
- aliases
- circular imports

## Useful Commands

Run alembic tests:

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_5.py
```

Run distillation tests:

```bash
python3 ft_distillation_0.py
python3 ft_distillation_1.py
```

Run transmutation tests:

```bash
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
```

Run circular dependency examples:

```bash
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

`ft_alembic_4.py` and `ft_kaboom_1.py` intentionally raise errors for learning.

Check style:

```bash
flake8 .
```

Check type hints:

```bash
mypy .
```

## Quick Notes

`import module` imports the module name.

`from module import function` imports one function directly.

`__init__.py` controls what a package exposes.

A relative import starts from the current package.

A circular import happens when two files import each other before they are ready.
