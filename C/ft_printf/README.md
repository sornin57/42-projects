*This project has been created as part of the 42 curriculum by msornin.*

# ft_printf

## Description

`ft_printf` is a small recreation of the standard `printf` function.
It reads a format string, detects `%` conversions, prints the matching argument,
and returns the number of characters written.

## Instructions

Build the library:

```sh
make
```

Clean generated files:

```sh
make fclean
```

## Supported Conversions

- `%c` prints one character.
- `%s` prints a string.
- `%p` prints a pointer address in hexadecimal.
- `%d` and `%i` print a signed integer.
- `%u` prints an unsigned integer.
- `%x` prints hexadecimal in lowercase.
- `%X` prints hexadecimal in uppercase.
- `%%` prints a percent sign.

## Algorithm

The function reads the format string from left to right. Normal characters are
printed directly with `write`. When a `%` is found, the next character decides
which type to fetch with `va_arg`. Numbers are printed recursively, digit by
digit, using base 10 or base 16.

## Resources

- `man 3 printf`
- `man 3 stdarg`
- `man 2 write`
