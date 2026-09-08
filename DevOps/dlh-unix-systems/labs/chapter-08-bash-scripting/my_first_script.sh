#!/bin/sh

user_name=${1:-student}
color=${2:-blue}
echo '=== Welcome to My First Script ==='
echo "Script name: $0"
echo "Current date: $(date)"
echo "Current user: $(whoami)"
echo "Current directory: $(pwd)"
echo "Hello $user_name! Your favorite color is $color."
