*This project has been created as part of the 42 curriculum by msornin.*

# Libft

## Description

Libft is the first C library project in the 42 curriculum. The goal is to
reimplement common libc functions, then add useful string, memory, output and
linked-list helpers.

This repository currently contains a compile-ready skeleton. The function bodies
are intentionally neutral stubs so each exercise can be implemented manually.

## Instructions

Build the library:

```bash
make
```

Clean object files:

```bash
make clean
```

Remove object files and `libft.a`:

```bash
make fclean
```

Rebuild from scratch:

```bash
make re
```

Run the 42 style checker:

```bash
norminette .
```

## Exercise Checklist

Part 1 - Libc functions:

- [ ] `ft_isalpha`
- [ ] `ft_isdigit`
- [ ] `ft_isalnum`
- [ ] `ft_isascii`
- [ ] `ft_isprint`
- [ ] `ft_strlen`
- [ ] `ft_memset`
- [ ] `ft_bzero`
- [ ] `ft_memcpy`
- [ ] `ft_memmove`
- [ ] `ft_strlcpy`
- [ ] `ft_strlcat`
- [ ] `ft_toupper`
- [ ] `ft_tolower`
- [ ] `ft_strchr`
- [ ] `ft_strrchr`
- [ ] `ft_strncmp`
- [ ] `ft_memchr`
- [ ] `ft_memcmp`
- [ ] `ft_strnstr`
- [ ] `ft_atoi`
- [ ] `ft_calloc`
- [ ] `ft_strdup`

Part 2 - Additional functions:

- [ ] `ft_substr`
- [ ] `ft_strjoin`
- [ ] `ft_strtrim`
- [ ] `ft_split`
- [ ] `ft_itoa`
- [ ] `ft_strmapi`
- [ ] `ft_striteri`
- [ ] `ft_putchar_fd`
- [ ] `ft_putstr_fd`
- [ ] `ft_putendl_fd`
- [ ] `ft_putnbr_fd`

Part 3 - Linked list:

- [ ] `ft_lstnew`
- [ ] `ft_lstadd_front`
- [ ] `ft_lstsize`
- [ ] `ft_lstlast`
- [ ] `ft_lstadd_back`
- [ ] `ft_lstdelone`
- [ ] `ft_lstclear`
- [ ] `ft_lstiter`
- [ ] `ft_lstmap`

## Resources

- `man 3` pages for libc behavior.
- 42 Norminette documentation and local `norminette` command.
- The local Libft subject PDF.
