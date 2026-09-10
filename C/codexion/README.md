*This project has been created as part of the 42 curriculum by msornin.*

# Codexion

## Description

Codexion is a concurrency simulation written in C. Several coders share a limited number of USB dongles. A coder needs two dongles to compile, then spends time debugging and refactoring before trying again.

The goal is to coordinate threads correctly, avoid mixed logs, avoid deadlocks, and stop the simulation when a coder burns out or when every coder has compiled enough times.

## Instructions

Compile the project:

```bash
make
```

Run the program:

```bash
./codexion number_of_coders time_to_burnout time_to_compile time_to_debug time_to_refactor number_of_compiles_required dongle_cooldown scheduler
```

Example with FIFO scheduling:

```bash
./codexion 4 800 200 200 200 3 0 fifo
```

Example with EDF scheduling:

```bash
./codexion 4 800 200 200 200 3 0 edf
```

Clean build files:

```bash
make clean
make fclean
make re
```

## Arguments

| Argument | Meaning |
| --- | --- |
| `number_of_coders` | Number of coder threads and number of dongles |
| `time_to_burnout` | Max time without starting a compile |
| `time_to_compile` | Time spent compiling while holding two dongles |
| `time_to_debug` | Time spent debugging after compiling |
| `time_to_refactor` | Time spent refactoring after debugging |
| `number_of_compiles_required` | Stop when all coders reach this count |
| `dongle_cooldown` | Delay before a released dongle can be reused |
| `scheduler` | `fifo` or `edf` |

## Blocking cases handled

- Deadlock prevention: coders take dongles in a fixed order by dongle id. This removes the circular wait case.
- Starvation reduction: each dongle keeps a waiting queue. FIFO uses arrival order, EDF uses the earliest burnout deadline.
- Cooldown handling: after release, a dongle stores the next time it can be used again.
- Precise burnout detection: a monitor thread checks coders regularly and stops the simulation when a deadline is missed.
- Log serialization: all messages pass through one print mutex, so lines do not mix together.
- Single coder case: one coder can take one dongle, but cannot compile because two dongles are required.

## Thread synchronization mechanisms

The project uses `pthread_create` to start one thread per coder and one monitor thread.

Each dongle has:

- a `pthread_mutex_t` to protect its state
- a `pthread_cond_t` to wake waiting coders
- a small binary heap for FIFO or EDF ordering

The global state has:

- a mutex for stop state and coder compile counters
- a mutex for log output
- a mutex for ticket generation used by FIFO ordering

Race conditions are avoided by locking before reading or modifying shared values such as dongle usage, cooldown time, stop state, and compile counters.

## Resources

- `man pthread_create`
- `man pthread_mutex_lock`
- `man pthread_cond_wait`
- `man gettimeofday`
- `man usleep`
- POSIX threads documentation
