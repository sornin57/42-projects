*This project has been created as part of the 42 curriculum by msornin.*

# Get Next Line

## Description

`get_next_line` returns one line at a time from a file descriptor.
The goal is to learn how `read`, heap allocation, and static variables work together.

## Instructions

Compile the mandatory files with:

```sh
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c
```

The project can be tested with different `BUFFER_SIZE` values.

## Rules

- Allowed functions: `read`, `malloc`, `free`.
- Forbidden: `libft`, `lseek`, global variables.
- Return the line with the final `\n`, except at EOF when the file does not end with `\n`.
- Return `NULL` when there is nothing left to read or when an error occurs.
- The code must work with different `BUFFER_SIZE` values.

## Algorithm Notes

The usual strategy is to keep the unread part of the previous call inside a static
variable. Each call reads into a buffer until a newline is found or EOF is reached.
Then the function returns the next line and keeps the remaining text for the next call.

## Resources

- `man 2 read`
- `man 3 malloc`
- `man 3 free`
- Static variables in C
