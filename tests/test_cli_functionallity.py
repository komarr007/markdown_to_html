from unittest import TestCase, main

import io
import contextlib

import sys
sys.path.append("D:\\learning apps\\md2html\\src\\markdown_converter")

from src.markdown_converter.cli import parse_arguments
from src.markdown_converter.cli import InvalidFileExtensionError

class TestCliInput(TestCase):
    """
    Base class for testing cli input.
    """

    def test_valid_argument(self):
        argv = ["test.md", "output.html", "--title", "document"]
        args_parser = parse_arguments(argv)
        
        self.assertEqual(args_parser.input_file, "test.md")
        self.assertEqual(args_parser.output_file, "output.html")
        self.assertEqual(args_parser.title, "document")

    def test_default_title_argument(self):
        argv = ["input.md", "output.html"]
        args = parse_arguments(argv)

        self.assertEqual(args.title, "Converted Markdown")

    def test_empty_argument_outputs_usage(self):
        argv = []

        with self.assertRaises(SystemExit) as context:
            with contextlib.redirect_stdout(io.StringIO()) as stdout, \
                 contextlib.redirect_stderr(io.StringIO()) as stderr:
                parse_arguments(argv)

        self.assertEqual(context.exception.code, 2)

        error_output = stderr.getvalue()
        self.assertIn("usage:", error_output)

    def test_invalid_argument(self):
        argv = ["input.md", "output.html", "--invalid-arg"]

        with self.assertRaises(SystemExit) as context:
            with contextlib.redirect_stdout(io.StringIO()) as stdout, \
                 contextlib.redirect_stderr(io.StringIO()) as stderr:
                parse_arguments(argv)

        self.assertEqual(context.exception.code, 2)

        error_output = stderr.getvalue()
        self.assertIn("unrecognized arguments: --invalid-arg", error_output)

    def test_invalid_file_extension(self):
        with self.assertRaises(InvalidFileExtensionError) as context:
            argv = ["input.txt", "output.html"]
            parse_arguments(argv)

        self.assertIn("Expected .md for input and .html for output", str(context.exception))

    def test_upper_file_extention(self):
        argv = ["input.MD", "output.HTML"]
        args = parse_arguments(argv)
        self.assertEqual(args.input_file, "input.MD")
        self.assertEqual(args.output_file, "output.HTML")

if __name__ == "__main__":
    main()