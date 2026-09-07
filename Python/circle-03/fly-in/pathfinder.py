"""Find valid shortest paths through the drone network."""
from __future__ import annotations

from models import Graph, Zone, ZoneType


def find_paths(graph: Graph, start: Zone, goal: Zone) -> list[list[Zone]]:
    """Return all valid shortest paths from start to goal."""
    queue = [[start]]
    paths: list[list[Zone]] = []
    shortest_length = None

    while queue:
        path = queue.pop(0)
        current_zone = path[-1]

        if shortest_length is not None and len(path) > shortest_length:
            continue

        if current_zone is goal:
            shortest_length = len(path)
            paths.append(path)
            continue

        neighbors = []

        for connexion in current_zone.connexions:
            neighbor = connexion.other_zone(current_zone)

            if neighbor in path:
                continue

            if neighbor.zone_type is ZoneType.BLOCKED:
                continue

            neighbors.append(neighbor)

        neighbors.sort(
            key=lambda zone: zone.zone_type is not ZoneType.PRIORITY
        )

        for neighbor in neighbors:
            new_path = path + [neighbor]
            queue.append(new_path)

    return paths
