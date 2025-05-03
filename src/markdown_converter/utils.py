import os

def get_base_dir():
    """
    Get the base directory of the project.
    """
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    split_path = dir_path.split("\\")

    del split_path[-2:]
    
    base_dir = "\\".join(split_path) + "\\"
    return base_dir

BASE_DIR = get_base_dir()