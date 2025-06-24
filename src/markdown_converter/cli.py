import argparse
from pathlib import Path

from markdown_converter.validations import validate_file_extensions

class InvalidFileExtensionError(Exception):
    """Custom exception for invalid file extensions."""
    def __init__(self, input_ext=None, output_ext=None, message=None):
        if message is None:
            self.message = (
                f"Expected .md for input and .html for output, "
                f"but got '{input_ext}' for input and '{output_ext}' for output"
                if input_ext and output_ext else
                "Invalid file extensions provided."
            )
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidFileExtensionError: {self.message}"

def parse_arguments(argv=None):
    """
    Parse command line arguments

    :argv: List of command line arguments
    """
    
    parser = argparse.ArgumentParser(description="Markdown to HTML Converter")
    parser.add_argument("input_file", type=str, help="Path to the input markdown file")
    parser.add_argument("output_file", type=str, help="Path to the output HTML file")
    parser.add_argument("--title", type=str, default="Converted Markdown",
        help="Title for the HTML document (default: 'Converted Markdown')")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args(argv)

    is_valid_file_extension = validate_file_extensions(args.input_file, 
                                                   args.output_file)
    if is_valid_file_extension:
        return args
    if not is_valid_file_extension:
        raise InvalidFileExtensionError(Path(args.input_file).suffix,
                                        Path(args.output_file).suffix)