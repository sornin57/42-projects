#!/bin/sh

WORK_DIR=${1:-permission_lab}

mkdir -p "$WORK_DIR"
touch "$WORK_DIR/public.txt" "$WORK_DIR/private.txt"
printf '%s\n' '#!/bin/sh' 'echo Permission demo script' > "$WORK_DIR/run_demo.sh"

chmod 644 "$WORK_DIR/public.txt"
chmod 600 "$WORK_DIR/private.txt"
chmod 755 "$WORK_DIR/run_demo.sh"

printf '%s\n' '=== Permissions ==='
ls -l "$WORK_DIR"
printf '\nCurrent umask: %s\n' "$(umask)"
printf 'Current user and groups:\n'
id
