import markdown
from utils import BASE_DIR


class MarkdownConverter:
    """
    Class to conver Markdown file to HTML.
    """
    def convert(self, input_file, output_file, title="Converted Markdown"):
        """
        Convert a markdown file to HTML.

        :param input_file: Path to the input markdown file
        :param output_file: Path to the output HTML file
        :param title: Title for the HTML document (default: 'Converted Markdown')
        """

        try:
            with open(input_file, 'r', encoding='utf-8') as md_file:
                text = md_file.read()

            html = markdown.markdown(text)

            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(f"<!DOCTYPE html>\n")
                html_file.write(f"<html lang='en>\n")
                html_file.write(f"<head><meta charset='UTF-8'>\n\
                                <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\
                                <title>{title}</title></head>\n")
                html_file.write(f"<body>{html}</body>\n</html>")

        except FileNotFoundError:
            print(f"Error: The file {input_file} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


input_file = BASE_DIR + "test_files/test.md"
output_file = BASE_DIR + "test_files/test.html"
obj = MarkdownConverter()
obj.convert(input_file, output_file, "Test Title")