from pathlib import Path

def get_base_dir():
    """
    Get the base directory of the project.
    """
    return Path(__file__).resolve().parent.parent

BASE_DIR = get_base_dir()