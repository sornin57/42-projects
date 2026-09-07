"""Test the main Fly-in parser, pathfinding, and simulation flows."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from models import Drone, ZoneType
from parser import MapError, read_map
from pathfinder import find_paths
from simulation import simulate


ROOT = Path(__file__).resolve().parents[1]


class FlyInTestCase(unittest.TestCase):
    """Cover representative project behavior."""

    def test_parser_loads_map_metadata(self) -> None:
        nb_drones, graph = read_map(
            str(ROOT / "maps/easy/02_simple_fork.txt")
        )

        junction = graph.find_zone("junction")

        self.assertEqual(nb_drones, 4)
        self.assertIsNotNone(graph.start_zone)
        self.assertIsNotNone(graph.end_zone)
        self.assertIsNotNone(junction)
        self.assertEqual(junction.max_drones, 2)
        self.assertEqual(len(graph.connexions), 5)

    def test_pathfinder_ignores_blocked_zones(self) -> None:
        _, graph = read_map(str(ROOT / "maps/easy/test_blocked.txt"))
        assert graph.start_zone is not None
        assert graph.end_zone is not None

        paths = find_paths(graph, graph.start_zone, graph.end_zone)
        path_names = [[zone.name for zone in path] for path in paths]

        self.assertEqual(path_names, [["start", "safe_path", "goal"]])
        self.assertEqual(
            graph.find_zone("blocked_path").zone_type,
            ZoneType.BLOCKED,
        )

    def test_simulation_moves_drones_turn_by_turn(self) -> None:
        nb_drones, graph = read_map(
            str(ROOT / "maps/easy/01_linear_path.txt")
        )
        assert graph.start_zone is not None
        assert graph.end_zone is not None

        paths = find_paths(graph, graph.start_zone, graph.end_zone)
        drones = [
            Drone(drone_id, graph.start_zone)
            for drone_id in range(1, nb_drones + 1)
        ]

        turns = simulate(drones, paths, graph)

        self.assertEqual(len(turns), 4)
        self.assertEqual(turns[-1], "D2-goal")

    def test_parser_rejects_unknown_connection_zone(self) -> None:
        invalid_map = "\n".join(
            [
                "nb_drones: 1",
                "start_hub: start 0 0",
                "end_hub: goal 1 0",
                "connection: start-missing",
            ]
        )

        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as file:
            file.write(invalid_map)
            file.flush()

            with self.assertRaises(MapError):
                read_map(file.name)


if __name__ == "__main__":
    unittest.main()
