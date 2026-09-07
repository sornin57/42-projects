# 42 Fly-in

Fly-in is a Python drone-traffic simulation project created as part of the 42 curriculum.

The program reads a map file, builds a graph of hubs and connections, finds valid paths between the start hub and the end hub, then moves drones turn by turn while respecting zone and connection capacities.

## What It Shows

- Graph modeling with zones and bidirectional connections
- Map parsing with explicit validation errors
- Breadth-first search pathfinding
- Turn-by-turn simulation
- Capacity constraints on hubs and connections
- Unit tests with `unittest`
- Python quality checks with `flake8` and `mypy`

## Project Structure

```txt
.
├── main.py
├── models.py
├── parser.py
├── pathfinder.py
├── simulation.py
├── maps/
├── tests/
│   └── test_flyin.py
└── Makefile
```

## Run

Run the default map:

```bash
make run
```

Run a specific map:

```bash
make run MAP=maps/easy/02_simple_fork.txt
```

Or call the program directly:

```bash
python3 main.py maps/easy/01_linear_path.txt
```

## Tests

Run the unit tests:

```bash
make test
```

The tests cover:

- map parsing
- blocked-zone avoidance
- turn-by-turn drone movement
- invalid map errors

## Lint And Type Checks

Create the virtual environment and install development tools:

```bash
make install
```

Run quality checks:

```bash
make lint
```

Run lint and tests together:

```bash
make check
```

## Map Format

Example:

```txt
nb_drones: 2

start_hub: start 0 0
hub: waypoint1 1 0
hub: waypoint2 2 0
end_hub: goal 3 0

connection: start-waypoint1
connection: waypoint1-waypoint2
connection: waypoint2-goal
```

Supported metadata:

```txt
[zone=blocked]
[zone=restricted]
[zone=priority]
[max_drones=2]
[max_link_capacity=2]
```

## Program Flow

```txt
map file
   |
   v
parser.py
   |
   |-- reads and validates the map
   |-- creates Zone objects
   |-- creates Connexion objects
   `-- fills the Graph object
          |
          v
pathfinder.py
   |
   `-- finds valid shortest paths with BFS
          |
          v
simulation.py
   |
   |-- assigns paths to drones
   |-- checks zone and link capacities
   |-- moves drones turn by turn
   `-- records each turn
          |
          v
main.py
   |
   `-- prints the simulation
```

## Interview Summary

Fly-in is a graph-based Python simulation. I parse a custom map format, build a graph, compute valid paths with breadth-first search, and simulate drone movement while respecting capacity constraints.
