#!/bin/sh

printf '%s\n' '=== Current Shell ==='
printf 'Shell PID: %s\n' "$$"

printf '\n%s\n' '=== Top CPU Processes ==='
ps aux --sort=-%cpu | head -6

printf '\n%s\n' '=== Top Memory Processes ==='
ps aux --sort=-%mem | head -6

printf '\n%s\n' '=== Process Count ==='
ps aux | wc -l
