#!/bin/sh

echo '=== awk columns ==='
awk -F',' '{print $2, $3}' data/users.csv
echo '=== developers ==='
awk -F',' '$3 == "Developer" {print $2}' data/users.csv
echo '=== log levels ==='
awk '{levels[$3]++} END {for (level in levels) print level, levels[level]}' data/system.log | sed 's/://g' | sort
echo '=== errors ==='
grep -E 'ERROR|CRITICAL' data/system.log
