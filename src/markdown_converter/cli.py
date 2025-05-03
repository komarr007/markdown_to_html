import argparse

class CommandLineInterface:
    """
    Command Line Interface for the Markdown to HTML Converter
    """
    parser = argparse.ArgumentParser(description="Markdown to HTML Converter")

    parser.add_argument(
        "input_file", type=str, help="Path to the input markdown file")
    parser.add_argument(
        "output_file", type=str, help="Path to the output HTML file")
    parser.add_argument(
        "--title", type=str, default="Converted Markdown",
        help="Title for the HTML document (default: 'Converted Markdown')")
    
    args = parser.parse_args()

    def __init__(self, input_file, output_file, title):
        self.input_file = input_file
        self.output_file = output_file
        self.title = title

    def convert(self):
        # Placeholder for conversion logic
        print(f"Converting {self.input_file} to {self.output_file} with title '{self.title}'")



obj = CommandLineInterface(
    input_file=CommandLineInterface.args.input_file,
    output_file=CommandLineInterface.args.output_file,
    title=CommandLineInterface.args.title
)

print(obj.convert())