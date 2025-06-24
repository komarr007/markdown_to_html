import unittest
import tempfile
import os

import sys
sys.path.append("D:\\learning apps\\md2html\\src\\markdown_converter")
from src.markdown_converter.cli import parse_arguments
from src.markdown_converter.converter import MarkdownConverter

class TestCliIntegration(unittest.TestCase):

    def test_full_cli_execution(self):
        # Step 1: create a temp markdown file
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".md", delete=False) as md:
            md.write("# Header\nThis is a CLI test.")
            md_path = md.name

        # Step 2: define output HTML file path
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as html:
            html_path = html.name

        # Step 3: create fake argv and run CLI logic
        argv = [md_path, html_path, "--title", "CLI Test Doc"]
        args = parse_arguments(argv)

        md_converter = MarkdownConverter

        result = md_converter.convert(
            args.input_file,
            args.output_file,
            title=args.title
        )

        try:
            # Step 4: Assert conversion result and file contents
            self.assertEqual(result["status"], "success")
            self.assertTrue(os.path.exists(html_path))

            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
                self.assertIn("<title>CLI Test Doc</title>", html)
                self.assertIn("<h1>Header</h1>", html)
                self.assertIn("<p>This is a CLI test.</p>", html)
        finally:
            os.remove(md_path)
            os.remove(html_path)

if __name__ == "__main__":
    unittest.main()
