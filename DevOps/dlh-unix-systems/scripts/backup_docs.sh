#!/bin/sh

SOURCE_DIR=${1:-notes}
BACKUP_DIR="backup_${SOURCE_DIR}_$(date +%Y%m%d)"

if [ ! -d "$SOURCE_DIR" ]; then
	printf 'Error: directory not found: %s\n' "$SOURCE_DIR" >&2
	exit 1
fi

cp -r "$SOURCE_DIR" "$BACKUP_DIR"
printf 'Backup created: %s\n' "$BACKUP_DIR"
