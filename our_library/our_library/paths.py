import os
import json

HEREDIR = os.path.dirname(os.path.abspath(__file__))  # path to this file
ROOT_DIR = os.path.dirname(os.path.dirname(HEREDIR))  # two levels up
RESULTS_DIR = os.path.join(ROOT_DIR, "results")


def get_results_subdir(subdir_name):
    """Get the path to a subfolder in the results directory."""
    path = os.path.join(RESULTS_DIR, subdir_name)
    os.makedirs(path, exist_ok=True)
    return path


def _add_json_extension(filepath):
    """Ensure filepath ends with .json, otherwise add it."""
    filepath = str(filepath)
    if not filepath.lower().endswith(".json"):
        filepath += ".json"
    return filepath


def save_json(data, filepath):
    """Save a Python object as a JSON file. Automatically creates parent
    folders if necessary, and appends .json if missing."""

    filepath = _add_json_extension(filepath)

    # Create parent directories if needed
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_json(filepath):
    """Load a JSON file and return its contents as a Python object.
    Appends .json if missing."""

    filepath = _add_json_extension(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
