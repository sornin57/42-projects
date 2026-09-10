# Piscine Python

Personal Python Piscine rebuilt module by module.

## Goal

Review Python fundamentals with clean folders, simple exercises, and short module summaries.

## Modules

- `Python00` - Basic functions, input/output, conditions, loops, recursion, and type hints.
- `Python01` - Object-oriented garden system with classes, methods, inheritance, encapsulation, and statistics.
- `Python02` - Exception handling and defensive programming with garden data validation.
- `Python03` - Python collections through lists, tuples, sets, dictionaries, generators, and comprehensions.
- `Python04` - File operations with read, write, streams, stderr, and context managers.
- `Python05` - Abstract processors, polymorphism, data streams, and export plugins.
- `Python06` - Python imports, packages, aliases, relative imports, and circular dependencies.
- `Python07` - Abstract factory, creature capabilities, and battle strategy pattern.
- `Python08` - Virtual environments, dependency management, and environment variables.
- `Python09` - Pydantic models, field validation, custom validators, and nested data.
- `Python10` - Functional programming with lambdas, closures, functools, and decorators.

## Testing

Each exercise is kept in its own folder.

Run a single exercise:

```bash
python3 ex0/file_name.py
```

Run all exercises from one module:

```bash
for file in ex*/*.py; do python3 "$file"; done
```

Check syntax:

```bash
python3 -m compileall .
```
