"""Run the Fly-in command-line application."""
from __future__ import annotations

import sys

from models import Drone, Graph
from parser import MapError, read_map
from pathfinder import find_paths
from simulation import simulate


RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"


def colorize_turn(turn: str, graph: Graph) -> str:
    """Add terminal colors to one simulation turn."""
    colored_moves: list[str] = []

    for movement in turn.split():
        if "-" not in movement:
            colored_moves.append(movement)
            continue

        route = movement.split("-", 1)[1]
        destination_name = route.rsplit("-", 1)[-1]
        zone = graph.find_zone(destination_name)

        color = WHITE

        if zone is graph.start_zone:
            color = GREEN
        elif zone is graph.end_zone:
            color = GREEN
        elif zone is not None:
            if zone.zone_type.value == "priority":
                color = CYAN
            elif zone.zone_type.value == "restricted":
                color = YELLOW
            elif zone.zone_type.value == "blocked":
                color = RED

        colored_moves.append(
            f"{color}{movement}{RESET}"
        )

    return " ".join(colored_moves)


def main() -> None:
    """Load the map, run the simulation, and print the results."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <map_file>")
        return

    map_file = sys.argv[1]

    try:
        nb_drones, graph = read_map(map_file)
    except MapError as error:
        print(f"Erreur : {error}")
        return

    start_zone = graph.start_zone
    goal_zone = graph.end_zone

    if start_zone is None or goal_zone is None:
        print("Erreur : start_hub ou end_hub introuvable")
        return

    paths = find_paths(graph, start_zone, goal_zone)

    if not paths:
        print("Erreur : aucun chemin disponible")
        return

    drones = [
        Drone(drone_id, start_zone)
        for drone_id in range(1, nb_drones + 1)
    ]

    turns = simulate(drones, paths, graph)

    for turn in turns:
        print(colorize_turn(turn, graph))

    print("Total turns:", len(turns))


if __name__ == "__main__":
    main()
