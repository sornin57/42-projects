#!/bin/sh

USERS_FILE=${1:-data/sample_users.csv}
LOG_FILE=${2:-data/sample_system.log}

if [ ! -f "$USERS_FILE" ] || [ ! -f "$LOG_FILE" ]; then
	printf '%s\n' 'Missing sample data files.' >&2
	exit 1
fi

printf '%s\n' '=== Users By Role ==='
awk -F',' '{roles[$3]++} END {for (role in roles) print role ":", roles[role]}' "$USERS_FILE" | sort

printf '\n%s\n' '=== Log Levels ==='
awk '{levels[$3]++} END {for (level in levels) print level, levels[level]}' "$LOG_FILE" | sed 's/://g' | sort

printf '\n%s\n' '=== Error Lines ==='
grep -E 'ERROR|CRITICAL' "$LOG_FILE"
