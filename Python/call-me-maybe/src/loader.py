"""JSON file loading utilities."""

import json
from pathlib import Path
from typing import Any


def load_json_file(path: str) -> Any:
    """Load and return data from a JSON file."""
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        raise ValueError(f"File not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON file: {path}") from error
