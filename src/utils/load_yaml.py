from typing import Any

import yaml


def parse_from_yaml(path_to_yaml: str) -> dict[Any, Any]:
    with open(path_to_yaml, "r", encoding="utf-8") as file:
        config: dict[Any, Any] = yaml.safe_load(file)
    return config
