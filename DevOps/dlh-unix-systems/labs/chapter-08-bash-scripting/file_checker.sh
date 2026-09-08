#!/bin/sh

if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1
echo "Checking: $filename"
if [ -f "$filename" ]; then
    echo "File exists"
elif [ -d "$filename" ]; then
    echo "Directory exists"
else
    echo "File or directory does not exist"
    exit 1
fi
[ -r "$filename" ] && echo "Readable" || echo "Not readable"
[ -w "$filename" ] && echo "Writable" || echo "Not writable"
[ -x "$filename" ] && echo "Executable" || echo "Not executable"
exit 0
