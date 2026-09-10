# Python03 - Data Quest

This module focuses on Python collections.

## Goal

Use the right data structure for the right job.

## Exercises

```text
ex0/ft_command_quest.py         - read command-line arguments
ex1/ft_score_analytics.py       - store scores in a list
ex2/ft_coordinate_system.py     - store 3D coordinates in tuples
ex3/ft_achievement_tracker.py   - compare achievements with sets
ex4/ft_inventory_system.py      - store inventory items in a dictionary
ex5/ft_data_stream.py           - generate events with yield
ex6/ft_data_alchemist.py        - transform data with comprehensions
```

## Concepts

- `sys.argv`
- lists
- tuples
- sets
- dictionaries
- generators
- `yield`
- list comprehensions
- dictionary comprehensions

## Useful Commands

Run command-line arguments:

```bash
python3 ex0/ft_command_quest.py hello world 42
```

Run score analytics:

```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800
```

Run coordinates:

```bash
python3 ex2/ft_coordinate_system.py
```

Run inventory:

```bash
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2
```

Run all non-interactive exercises:

```bash
python3 ex0/ft_command_quest.py hello world
python3 ex1/ft_score_analytics.py 1500 2300 1800
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2
python3 ex5/ft_data_stream.py
python3 ex6/ft_data_alchemist.py
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

A list keeps ordered data that can change.

A tuple keeps ordered data that should not change.

A set keeps unique values and is useful for comparisons.

A dictionary stores key-value pairs.

A generator creates values one by one with `yield`.

A comprehension creates a new list, set, or dictionary in a compact way.
