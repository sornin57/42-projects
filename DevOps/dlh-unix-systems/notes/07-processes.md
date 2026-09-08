# Processes And Jobs

A process is a running program. Each process has a PID, a parent process, an owner, and a current state.

## Process States

```text
R = running
S = sleeping
T = stopped
Z = zombie
```

## Inspect Processes

```bash
ps
ps aux
ps -ef
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
echo $$
```

## Real-Time Monitoring

```bash
top
htop
```

In `top`:

```text
q = quit
P = sort by CPU
M = sort by memory
k = kill process
```

## Signals

```text
SIGTERM = ask process to stop cleanly
SIGKILL = force stop
SIGINT  = Ctrl+C
SIGSTOP = pause
SIGCONT = continue
```

## Kill Commands

```bash
kill PID
kill -9 PID
pgrep process_name
pkill process_name
killall process_name
```

Use `kill -9` only when a normal stop does not work.

## Background Jobs

```bash
sleep 300 &
jobs
fg %1
bg %1
kill %1
```

`Ctrl+Z` suspends a foreground process. `fg` brings it back.
