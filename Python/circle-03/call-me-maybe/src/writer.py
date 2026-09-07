"""JSON output writing utilities."""

import json
from pathlib import Path

from src.models import FunctionCallResult


def write_results(
    path: str,
    results: list[FunctionCallResult],
) -> None:
    """Write validated function-call results to a JSON file."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = [result.model_dump() for result in results]

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
