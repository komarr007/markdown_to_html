import unittest
import subprocess
import tempfile
import os
from pathlib import Path

class TestMd2HtmlSubprocess(unittest.TestCase):
    def test_md2html_cli_conversion(self):

        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", 
                                        delete=False) as md_file:
            md_file.write("# Hello from subprocess\nThis is tested through CLI")
            input_path = md_file.name

        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as html_file:
            output_path = html_file.name

        try:
            result = subprocess.run(
                ["md2html", input_path, output_path, "--title", "Subprocess Test"],
                capture_output=True,
                text=True,
                check=False
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)

            with open(output_path, "r", encoding="utf-8") as f:
                html = f.read()
                self.assertIn("<title>Subprocess Test</title>", html)
                self.assertIn("<h1>Hello from subprocess</h1>", html)
                self.assertIn("<p>This is tested through CLI</p>", html)

        finally:
            for file in [input_path, output_path]:
                os.remove(file)

if __name__ == "__main__":
    unittest.main()