# DLH UNIX Systems Initiation

Status: Completed / Certified  
Date: September 8, 2026  
Provider: Digital Learning Hub

## Overview

This module covers the fundamentals of working with UNIX/Linux systems from the command line. The goal is to become comfortable navigating the filesystem, managing files, editing text in the terminal, redirecting command output, combining tools with pipes, managing permissions, monitoring processes, and writing basic Bash scripts.

## Topics

- Command-line basics
- Filesystem navigation
- File and directory management
- Vim fundamentals
- Standard streams and redirections
- Pipes and text filtering with grep
- File permissions and ownership
- Process and job management
- Bash scripting fundamentals
- Text processing with awk and sed
- Command history and aliases

## Project Structure

```text
.
├── data/
│   ├── sample_access.log
│   ├── sample_system.log
│   └── sample_users.csv
├── notes/
│   ├── 01-cli-basics.md
│   ├── 02-filesystem.md
│   ├── 03-files.md
│   ├── 04-vim.md
│   ├── 05-pipes-grep.md
│   ├── 06-permissions.md
│   ├── 07-processes.md
│   ├── 08-bash-scripting.md
│   └── 09-advanced-tools.md
└── scripts/
    ├── backup_docs.sh
    ├── file_checker.sh
    ├── log_analysis.sh
    ├── permission_demo.sh
    ├── process_snapshot.sh
    ├── system_report.sh
    └── text_tools_report.sh
```

## Scripts

- `system_report.sh`: displays basic system information.
- `backup_docs.sh`: creates a dated backup of a directory.
- `log_analysis.sh`: extracts useful information from an access log.
- `permission_demo.sh`: creates sample files with different permissions.
- `process_snapshot.sh`: displays a quick process overview.
- `file_checker.sh`: checks file type and access permissions.
- `text_tools_report.sh`: uses awk, sed, and grep to summarize sample data.

## Skills Practiced

This project demonstrates basic Linux administration habits: clean folder structure, readable scripts, permission management, process inspection, command chaining, and practical use of standard command-line tools.

## Practical Labs



The `labs/` folder contains clean reproductions of the practical exercises from chapters 1 to 9.
