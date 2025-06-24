from markdown_converter.cli import parse_arguments
from markdown_converter.converter import MarkdownConverter

import sys

def main():
    """
    Main function to run the CLI
    """

    try:
        args = parse_arguments()
        convert = MarkdownConverter.convert(args.input_file,
                                            args.output_file, title=args.title)
        if convert['status'] == "success":
            print("Conversion successful")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()