# Bash Scripting

A shell script is a file containing commands executed by the shell.

## Script Structure

```bash
#!/bin/bash

echo "Hello, World!"
```

Run it:

```bash
chmod +x script.sh
./script.sh
```

Or run it directly with Bash:

```bash
bash script.sh
```

## Variables

```bash
name="Alice"
today=$(date)
echo "Hello, $name"
```

No spaces around `=` when assigning a variable.

## Arguments

```bash
echo "Script name: $0"
echo "First argument: $1"
echo "Number of arguments: $#"
echo "All arguments: $@"
```

## Conditions

```bash
if [ -f "$1" ]; then
	echo "File exists"
else
	echo "File not found"
fi
```

Useful tests:

```text
-f file exists and is a file
-d directory exists
-r readable
-w writable
-x executable
-z empty string
-n non-empty string
```

## Loops

```bash
for file in *.txt; do
	echo "$file"
done
```

```bash
while read line; do
	echo "$line"
done < input.txt
```

## Functions

```bash
log_message() {
	level=$1
	message=$2
	echo "[$level] $message"
}

log_message "INFO" "Script started"
```

## Safer Scripts

```bash
set -euo pipefail
```

This stops the script on errors, undefined variables, and failed commands inside pipes.
