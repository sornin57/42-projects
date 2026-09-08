# Advanced Tools And Productivity

This chapter focuses on `awk`, `sed`, history, aliases, and building faster command-line habits.

## awk

`awk` reads text line by line and works well with columns.

```bash
awk '{print $1}' file.txt
awk '{print $NF}' file.txt
awk -F',' '{print $2}' data.csv
awk '{print NR, $0}' file.txt
```

Useful variables:

```text
$0 = full line
$1 = first field
$NF = last field
NR = current line number
NF = number of fields
```

## sed

`sed` edits text streams.

```bash
sed 's/old/new/' file.txt
sed 's/old/new/g' file.txt
sed '/pattern/d' file.txt
sed -n '10,20p' file.txt
```

`g` means replace every occurrence on the line.

## History

```bash
history
!!
!123
Ctrl+R
```

Shortcuts:

```text
Ctrl+A = beginning of line
Ctrl+E = end of line
Ctrl+U = delete before cursor
Ctrl+K = delete after cursor
Ctrl+C = interrupt
Ctrl+Z = suspend
Ctrl+L = clear screen
```

## Aliases

```bash
alias ll='ls -la'
alias gs='git status'
alias gp='git push'
unalias ll
```

To keep aliases permanently, put them in `~/.bash_aliases` or `~/.bashrc`.
