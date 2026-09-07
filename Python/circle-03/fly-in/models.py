"""Define the core data models used by the Fly-in simulation."""
from __future__ import annotations

from enum import Enum


class ZoneType(Enum):
    """List the supported zone behaviors."""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class Zone:
    """Represent a hub in the drone network."""
    def __init__(
        self,
        name: str,
        x: int,
        y: int,
        zone_type: ZoneType,
        max_drones: int | None = None,
    ) -> None:
        """Initialize a zone with its properties and capacity."""
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.max_drones = max_drones
        self.connexions: list["Connexion"] = []

    def add_connection(
        self,
        connexion: "Connexion",
    ) -> None:
        """Attach a connection to this zone."""
        self.connexions.append(connexion)


class Connexion:
    """Represent a bidirectional link between two zones."""
    def __init__(
        self,
        zone_a: Zone,
        zone_b: Zone,
        max_link_capacity: int | None = None,
    ) -> None:
        """Initialize a connection and its capacity."""
        self.zone_a = zone_a
        self.zone_b = zone_b
        self.max_link_capacity = max_link_capacity

    def other_zone(self, zone: Zone) -> Zone:
        """Return the zone on the opposite side of the connection."""
        if zone is self.zone_a:
            return self.zone_b
        return self.zone_a


class Graph:
    """Store all zones and connections of a parsed map."""
    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.zones: list[Zone] = []
        self.connexions: list[Connexion] = []
        self.start_zone: Zone | None = None
        self.end_zone: Zone | None = None

    def add_zone(self, zone: Zone) -> None:
        """Add a zone to the graph."""
        self.zones.append(zone)

    def add_connection(self, connexion: Connexion) -> None:
        """Add a connection to the graph."""
        self.connexions.append(connexion)

    def find_zone(self, name: str) -> Zone | None:
        """Return a zone by name, or None if absent."""
        for zone in self.zones:
            if zone.name == name:
                return zone
        return None

    def find_connection(
        self,
        zone_a: Zone,
        zone_b: Zone,
    ) -> Connexion | None:
        """Return the connection linking two zones in either direction."""
        for connexion in self.connexions:
            same_direction = (
                connexion.zone_a is zone_a
                and connexion.zone_b is zone_b
            )
            opposite_direction = (
                connexion.zone_a is zone_b
                and connexion.zone_b is zone_a
            )

            if same_direction or opposite_direction:
                return connexion

        return None


class Drone:
    """Represent a drone and its current simulation state."""
    def __init__(self, drone_id: int, start_zone: Zone) -> None:
        """Initialize a drone at the given start zone."""
        self.drone_id = drone_id
        self.current_zone = start_zone
        self.path: list[Zone] = []
        self.path_index = 0
        self.wait_turns = 0
        self.transit_target: Zone | None = None
        self.transit_connection: Connexion | None = None
