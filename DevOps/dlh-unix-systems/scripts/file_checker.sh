#!/bin/sh

if [ $# -eq 0 ]; then
	printf 'Usage: %s <path>\n' "$0"
	exit 1
fi

TARGET=$1

if [ -f "$TARGET" ]; then
	printf 'File: %s\n' "$TARGET"
elif [ -d "$TARGET" ]; then
	printf 'Directory: %s\n' "$TARGET"
else
	printf 'Not found: %s\n' "$TARGET" >&2
	exit 1
fi

[ -r "$TARGET" ] && printf '%s\n' 'Readable: yes' || printf '%s\n' 'Readable: no'
[ -w "$TARGET" ] && printf '%s\n' 'Writable: yes' || printf '%s\n' 'Writable: no'
[ -x "$TARGET" ] && printf '%s\n' 'Executable: yes' || printf '%s\n' 'Executable: no'
