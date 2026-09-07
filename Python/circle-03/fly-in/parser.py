"""Parse Fly-in map files and build graph objects."""
from __future__ import annotations

from models import Connexion, Graph, Zone, ZoneType


class MapError(Exception):
    """Represent an invalid or unreadable map."""
    pass


def get_nb_drones(line: str) -> int:
    """Parse and validate the number of drones."""
    try:
        value = line.split(":", 1)[1].strip()
        nb_drones = int(value)
    except (IndexError, ValueError) as error:
        raise MapError("nb_drones invalide") from error

    if nb_drones <= 0:
        raise MapError("nb_drones doit être supérieur à 0")

    return nb_drones


def get_max_drones(parts: list[str]) -> int | None:
    """Parse and validate a zone capacity."""
    for part in parts[3:]:
        clean_part = part.strip("[]")

        if clean_part.startswith("max_drones="):
            try:
                return int(clean_part.split("=", 1)[1])
            except ValueError as error:
                raise MapError("max_drones invalide") from error

    return None


def get_zone_type(parts: list[str]) -> ZoneType:
    """Parse the optional zone type metadata."""
    for part in parts[3:]:
        clean_part = part.strip("[]")

        if clean_part.startswith("zone="):
            value = clean_part.split("=", 1)[1]

            if value == "blocked":
                return ZoneType.BLOCKED
            if value == "restricted":
                return ZoneType.RESTRICTED
            if value == "priority":
                return ZoneType.PRIORITY
            if value == "normal":
                return ZoneType.NORMAL

            raise MapError(f"Type de zone invalide : {value}")

    return ZoneType.NORMAL


def create_zone(line: str, graph: Graph) -> Zone:
    """Create a zone from one map line."""
    try:
        data = line.split(":", 1)[1].strip()
        parts = data.split()

        name = parts[0]
        x = int(parts[1])
        y = int(parts[2])
    except (IndexError, ValueError) as error:
        raise MapError(f"Zone invalide : {line}") from error

    if graph.find_zone(name) is not None:
        raise MapError(f"Zone dupliquée : {name}")

    max_drones = get_max_drones(parts)

    if line.startswith("hub:") and max_drones is None:
        max_drones = 1

    if line.startswith(("start_hub:", "end_hub:")):
        max_drones = None

    zone_type = get_zone_type(parts)

    zone = Zone(
        name,
        x,
        y,
        zone_type,
        max_drones,
    )

    graph.add_zone(zone)
    return zone


def get_link_capacity(parts: list[str]) -> int | None:
    """Parse and validate a connection capacity."""
    for part in parts[1:]:
        clean_part = part.strip("[]")

        if clean_part.startswith("max_link_capacity="):
            try:
                capacity = int(clean_part.split("=", 1)[1])
            except ValueError as error:
                raise MapError(
                    "max_link_capacity invalide"
                ) from error

            if capacity <= 0:
                raise MapError(
                    "max_link_capacity doit être supérieur à 0"
                )

            return capacity

    return 1


def read_map(filename: str) -> tuple[int, Graph]:
    """Read a map file and return its drone count and graph."""
    nb_drones = 0
    graph = Graph()

    try:
        file = open(filename, "r", encoding="utf-8")
    except FileNotFoundError as error:
        raise MapError(f"Fichier introuvable : {filename}") from error
    except PermissionError as error:
        raise MapError(f"Accès refusé : {filename}") from error

    with file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                if line.startswith("nb_drones:"):
                    nb_drones = get_nb_drones(line)

                elif line.startswith("start_hub:"):
                    if graph.start_zone is not None:
                        raise MapError(
                            "Plusieurs start_hub sont définis"
                        )

                    graph.start_zone = create_zone(
                        line,
                        graph,
                    )

                elif line.startswith("end_hub:"):
                    if graph.end_zone is not None:
                        raise MapError(
                            "Plusieurs end_hub sont définis"
                        )

                    graph.end_zone = create_zone(
                        line,
                        graph,
                    )

                elif line.startswith("hub:"):
                    create_zone(line, graph)

                elif line.startswith("connection:"):
                    connect = line.split(":", 1)[1].strip()
                    parts = connect.split()
                    zone_names = parts[0].split("-")

                    if len(zone_names) != 2:
                        raise MapError(
                            f"Connexion invalide : {line}"
                        )

                    zone_a = graph.find_zone(zone_names[0])
                    zone_b = graph.find_zone(zone_names[1])

                    if zone_a is None or zone_b is None:
                        raise MapError(
                            "Connexion vers une zone inconnue : "
                            f"{zone_names[0]}-{zone_names[1]}"
                        )

                    max_link_capacity = get_link_capacity(parts)

                    connexion = Connexion(
                        zone_a,
                        zone_b,
                        max_link_capacity,
                    )

                    graph.add_connection(connexion)
                    zone_a.add_connection(connexion)
                    zone_b.add_connection(connexion)

                else:
                    raise MapError(f"Ligne inconnue : {line}")

            except MapError as error:
                raise MapError(
                    f"Ligne {line_number} : {error}"
                ) from error

    if nb_drones <= 0:
        raise MapError("nb_drones manquant ou invalide")

    if graph.find_zone("start") is None:
        raise MapError("Zone start introuvable")

    if graph.end_zone is None:
        raise MapError("end_hub introuvable")

    return nb_drones, graph
