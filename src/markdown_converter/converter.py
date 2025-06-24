import markdown

class MarkdownConverter:
    """
    Class to conver Markdown file to HTML.
    """
    @staticmethod
    def convert(input_file, output_file, title="Converted Markdown"):
        """
        Convert a markdown files to HTML.

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
                html_file.write(f"<html lang='en'>\n")
                html_file.write(f"<head><meta charset='UTF-8'>\n\
                                <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\
                                <title>{title}</title></head>\n")
                html_file.write(f"<body>{html}</body>\n</html>")

            return {"status": "success",
                    "output_file": output_file}

        except FileNotFoundError:
            raise FileNotFoundError(f"The file {input_file} was not found.")
        except Exception as e:
            raise RuntimeError(f"Failed to convert markdown: {e}")


if __name__ == "__main__":
    converter = MarkdownConverter()