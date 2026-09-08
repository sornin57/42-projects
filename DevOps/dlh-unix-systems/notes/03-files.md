# Files And Directories

Basic file management is essential for working on a server.

## Commands

```bash
touch file.txt
cp file.txt copy.txt
mv copy.txt renamed.txt
rm renamed.txt
```

## Search

```bash
find . -type f
find . -name "*.sh"
```

## Count

```bash
wc -l file.txt
find . -type f | wc -l
```

`wc` means word count. With `-l`, it counts lines.
