#!/bin/sh

mkdir -p permission_test/secure_dir
touch permission_test/public_document.txt
touch permission_test/private_file.txt
printf '%s\n' '#!/bin/sh' 'echo Hello from script' > permission_test/test_script.sh
chmod 644 permission_test/public_document.txt
chmod 600 permission_test/private_file.txt
chmod 755 permission_test/test_script.sh
chmod 700 permission_test/secure_dir
ls -la permission_test
umask
umask -S 2>/dev/null || true
id
groups
