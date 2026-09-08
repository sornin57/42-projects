# Filesystem

UNIX systems organize files in a tree starting from `/`.

## Important Paths

- `/`: root directory.
- `~`: current user's home directory.
- `.`: current directory.
- `..`: parent directory.

## Navigation

```bash
pwd
cd ~
cd ..
ls -la
```

## Creating Directories

```bash
mkdir projects
mkdir -p training/linux/module01
```

`mkdir -p` creates parent directories when they do not already exist.
