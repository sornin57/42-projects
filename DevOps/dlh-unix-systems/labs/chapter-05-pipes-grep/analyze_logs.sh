#!/bin/sh

grep "ERROR" data/logs/error.log > reports/errors_only.txt
cut -d ' ' -f 1 data/logs/access.log | sort | uniq -c > reports/ip_count.txt
awk '{print $NF}' data/logs/access.log | sort | uniq -c > reports/status_count.txt
cat reports/errors_only.txt
cat reports/ip_count.txt
cat reports/status_count.txt
