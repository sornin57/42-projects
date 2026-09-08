#!/bin/sh

printf '%s\n' '=== Shell PID ==='
echo $$
printf '%s\n' '=== Process Count ==='
ps aux | wc -l
printf '%s\n' '=== Top CPU ==='
ps aux --sort=-%cpu | head -6
printf '%s\n' '=== Top Memory ==='
ps aux --sort=-%mem | head -6
