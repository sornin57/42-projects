# Python04 - Data Archivist

This module focuses on file operations.

## Goal

Learn how to open files, read data, write data, use standard streams, and close
resources safely.

## Exercises

```text
ex0/ft_ancient_text.py        - read and display a file
ex1/ft_archive_creation.py    - transform file content and save it
ex2/ft_stream_management.py   - use stdin, stdout, and stderr
ex3/ft_vault_security.py      - use with to close files automatically
```

## Concepts

- `open`
- `read`
- `write`
- `close`
- `sys.stdin`
- `sys.stdout`
- `sys.stderr`
- `with`
- exceptions during file operations

## Useful Commands

Create a sample file:

```bash
printf "line one\nline two\n" > ancient_fragment.txt
```

Run one exercise:

```bash
python3 ex0/ft_ancient_text.py ancient_fragment.txt
```

Run archive creation without saving:

```bash
printf "\n" | python3 ex1/ft_archive_creation.py ancient_fragment.txt
```

Run stream management:

```bash
printf "new_fragment.txt\n" | python3 ex2/ft_stream_management.py ancient_fragment.txt
```

Run vault security:

```bash
python3 ex3/ft_vault_security.py
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

`open()` gives access to a file.

`read()` gets the file content.

`write()` puts text inside a file.

`close()` releases the file.

`with open(...)` closes the file automatically, even if an error happens.
