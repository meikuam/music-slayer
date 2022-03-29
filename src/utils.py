import os
import json
from pathlib import Path


def project_root() -> Path:
    return Path(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )


with open(os.path.join(project_root(), "config.json")) as f:
    config = json.load(f)
