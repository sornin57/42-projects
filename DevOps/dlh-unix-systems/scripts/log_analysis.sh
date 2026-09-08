#!/bin/sh

LOG_FILE=${1:-data/sample_access.log}

if [ ! -f "$LOG_FILE" ]; then
	printf 'Error: log file not found: %s\n' "$LOG_FILE" >&2
	exit 1
fi

printf '%s\n' '=== Most Active IPs ==='
cut -d ' ' -f 1 "$LOG_FILE" | sort | uniq -c | sort -nr

printf '\n%s\n' '=== HTTP Status Codes ==='
awk '{print $NF}' "$LOG_FILE" | sort | uniq -c | sort -nr

printf '\n%s\n' '=== Admin Requests ==='
grep -i '/admin' "$LOG_FILE" || true
