from pathlib import Path

def is_markdown(file_path: str) -> bool:
    return Path(file_path).suffix.lower() == ".md"

def is_html(file_path: str) -> bool:
    return Path(file_path).suffix.lower() == ".html"

def validate_file_extensions(input_path: str, output_path: str) -> bool:
    return is_markdown(input_path) and is_html(output_path)