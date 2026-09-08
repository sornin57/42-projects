#!/bin/sh

printf '%s\n' '=== System Information ==='
printf 'Hostname: %s\n' "$(hostname)"
printf 'Current User: %s\n' "$(whoami)"
printf 'Current Date: %s\n' "$(date)"
printf '%s\n' 'Uptime:'
uptime
printf '%s\n' 'Disk Usage:'
df -h /
printf '%s\n' 'Memory Usage:'
free -h 2>/dev/null || vm_stat
printf '%s\n' '=== End Of Report ==='
