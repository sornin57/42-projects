# Pipes And Grep

Pipes and redirections make small commands work together.

## Redirections

```bash
command > file.txt      # write output, replacing the file
command >> file.txt     # append output
command 2> errors.txt   # write errors
command > all.txt 2>&1  # write output and errors together
```

## Pipes

```bash
command1 | command2
```

The output of `command1` becomes the input of `command2`.

## Grep

```bash
grep "ERROR" file.log
grep -i "error" file.log
grep -n "ERROR" file.log
grep -c "ERROR" file.log
```

## Example

```bash
cut -d ' ' -f 1 data/sample_access.log | sort | uniq -c
```

This command extracts the first column, sorts it, then counts repeated values.
