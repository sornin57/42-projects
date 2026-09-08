# Permissions And Ownership

UNIX permissions define who can read, write, or execute a file.

## Permission Types

```text
r = read
w = write
x = execute
```

## User Categories

```text
u = user / owner
g = group
o = others
a = all
```

## Reading Permissions

Example:

```text
-rw-r--r--
```

This means:

```text
owner: read + write
group: read only
others: read only
```

## Numeric Permissions

```text
read = 4
write = 2
execute = 1
```

Common values:

```bash
chmod 644 file.txt      # owner can write, everyone can read
chmod 755 script.sh     # executable script
chmod 700 private_dir   # owner only
chmod 600 secret.txt    # private file
```

## Ownership

```bash
ls -l file.txt
id
groups
chgrp group file.txt
sudo chown user:group file.txt
```

## Umask

`umask` controls default permissions for new files and directories.

```bash
umask
umask -S
umask 022
umask 077
```

A stricter umask like `077` creates private files by default.
