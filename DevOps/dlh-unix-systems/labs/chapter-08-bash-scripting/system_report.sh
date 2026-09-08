#!/bin/sh

log_message() {
    level=$1
    message=$2
    echo "[$level] $message"
}

for item in hostname uptime "df -h /" whoami; do
    log_message INFO "Running: $item"
    sh -c "$item"
done
