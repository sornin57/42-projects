"""Simulate drone movement turn by turn."""
from __future__ import annotations

from models import Connexion, Drone, Graph, Zone, ZoneType


def simulate(
    drones: list[Drone],
    paths: list[list[Zone]],
    graph: Graph,
) -> list[str]:
    """Move drones while respecting zones and connection capacities."""
    turns: list[str] = []

    for index, drone in enumerate(drones):
        drone.path = paths[index % len(paths)].copy()
        drone.path_index = 0
        drone.transit_target = None
        drone.transit_connection = None

    while any(
        drone.transit_target is not None
        or drone.path_index < len(drone.path) - 1
        for drone in drones
    ):
        moves: list[str] = []

        used_connections: dict[Connexion, int] = {}
        zone_occupancy: dict[Zone, int] = {}
        reserved_zones: dict[Zone, int] = {}

        for drone in drones:
            if drone.transit_target is None:
                current_count = zone_occupancy.get(
                    drone.current_zone,
                    0,
                )
                zone_occupancy[drone.current_zone] = (
                    current_count + 1
                )
            else:
                target = drone.transit_target
                connection = drone.transit_connection

                reserved_zones[target] = (
                    reserved_zones.get(target, 0) + 1
                )

                if connection is not None:
                    used_connections[connection] = (
                        used_connections.get(connection, 0) + 1
                    )

        # Les drones déjà en transit arrivent ce tour-ci.
        for drone in drones:
            if drone.transit_target is None:
                continue

            target = drone.transit_target

            drone.current_zone = target
            drone.path_index += 1
            drone.transit_target = None
            drone.transit_connection = None

            reserved_zones[target] -= 1
            zone_occupancy[target] = (
                zone_occupancy.get(target, 0) + 1
            )

            moves.append(
                f"D{drone.drone_id}-{target.name}"
            )

        # Les autres drones essaient de se déplacer.
        for drone in drones:
            if drone.transit_target is not None:
                continue

            if drone.path_index >= len(drone.path) - 1:
                continue

            # Un drone arrivé depuis une connexion restricted
            # ne repart pas pendant le même tour.
            arrival = f"D{drone.drone_id}-{drone.current_zone.name}"

            if arrival in moves:
                continue

            current_zone = drone.current_zone
            next_zone = drone.path[drone.path_index + 1]

            connection = graph.find_connection(
                current_zone,
                next_zone,
            )

            if connection is None:
                continue

            used = used_connections.get(connection, 0)
            link_capacity = connection.max_link_capacity

            if (
                link_capacity is not None
                and used >= link_capacity
            ):
                continue

            occupied = zone_occupancy.get(next_zone, 0)
            reserved = reserved_zones.get(next_zone, 0)
            zone_capacity = next_zone.max_drones

            if (
                zone_capacity is not None
                and occupied + reserved >= zone_capacity
            ):
                continue

            if next_zone.zone_type is ZoneType.RESTRICTED:
                drone.transit_target = next_zone
                drone.transit_connection = connection

                zone_occupancy[current_zone] -= 1
                reserved_zones[next_zone] = reserved + 1
                used_connections[connection] = used + 1

                moves.append(
                    f"D{drone.drone_id}-"
                    f"{current_zone.name}-{next_zone.name}"
                )
                continue

            zone_occupancy[current_zone] -= 1
            zone_occupancy[next_zone] = occupied + 1
            used_connections[connection] = used + 1

            drone.current_zone = next_zone
            drone.path_index += 1

            moves.append(
                f"D{drone.drone_id}-{next_zone.name}"
            )

        if not moves:
            break

        turns.append(" ".join(moves))

    return turns
