import unittest
import tempfile
import os

from unittest.mock import patch

from src.markdown_converter.converter import MarkdownConverter

class TestMarkdownConverter(unittest.TestCase):

    def test_successful_conversion(self):
        # Create a temporary markdown file
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".md", delete=False) as md:
            md.write("# Hello World\nThis is a test.")
            md_path = md.name

        # Create a temporary output file path
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as html:
            html_path = html.name

        try:
            # Run the converter
            result = MarkdownConverter.convert(md_path, html_path, title="Test Page")

            # Check result
            self.assertEqual(result["status"], "success")
            self.assertTrue(os.path.exists(html_path))

            # Check the contents of the generated HTML file
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn("<title>Test Page</title>", content)
                self.assertIn("<h1>Hello World</h1>", content)
                self.assertIn("<p>This is a test.</p>", content)

        finally:
            os.remove(md_path)
            os.remove(html_path)

    def test_input_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            MarkdownConverter.convert("nonexistent.md", "some_output.html")
    
    @patch("markdown_converter.converter.markdown.markdown", side_effect=Exception("boom"))
    def test_markdown_exception_handling(self, mock_md):
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".md", delete=False) as md:
            md.write("Hello")
            md_path = md.name

        try:
            with self.assertRaises(RuntimeError):
                MarkdownConverter.convert(md_path, "out.html")
        finally:
            os.remove(md_path)

    def test_output_write_failure(self):
        # Valid markdown input
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".md", delete=False) as md:
            md.write("Hello")
            md_path = md.name

        # Invalid output path (folder doesn't exist)
        bad_output_path = "this/folder/does/not/exist/output.html"

        try:
            with self.assertRaises((FileNotFoundError, OSError)):
                MarkdownConverter.convert(md_path, bad_output_path)
        finally:
            os.remove(md_path)

if __name__ == "__main__":
    unittest.main()
