# 📝 md2html — Markdown to HTML Converter CLI

**md2html** is a lightweight, fast, and tested Python CLI tool to convert Markdown files into responsive HTML documents — perfect for documentation, personal notes, or blog posts.

---

## ✨ Features

- 🧠 Simple and intuitive CLI interface
- ✅ Validates input/output file extensions
- ⚡ Converts `.md` to fully formatted `.html`
- 🧪 Fully tested: unit, integration, subprocess
- 🔌 Installable with `pip install -e .` using modern `pyproject.toml`

---

## 📦 Installation

Clone the repo and install it locally in **editable mode**:

```bash
git clone https://github.com/komarr007/md2html.git
cd md2html
pip install -e .
```

This will expose a global command:

```bash
md2html --help
```

---

## 🚀 Usage

```bash
md2html <input_file>.md <output_file>.html [--title "My HTML Title"]
```

### 🔧 Example

```bash
md2html docs/readme.md docs/readme.html --title "My Converted Page"
```

This will generate an HTML file with a `<title>`, clean layout, and all Markdown converted.

---

## 📁 Project Structure

```
md2html/
├── src/
│   └── markdown_converter/
│       ├── cli.py
│       ├── converter.py
│       ├── main.py
│       ├── validations.py
│       └── ...
├── tests/
│   ├── cli_test.py
│   ├── test_converter.py
│   ├── test_cli_subprocess.py
│   └── ...
├── pyproject.toml
└── README.md
```

---

## 🧪 Running Tests

Run all tests using `unittest`:

```bash
python -m unittest discover tests
```

Want a test that simulates the real command-line experience?

```bash
python -m unittest tests.test_cli_subprocess
```

---

## 📊 (Optional) Code Coverage

```bash
pip install coverage
coverage run -m unittest
coverage report -m
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Developed by **Rigaqi** — as part of a personal mission to write cleaner, more testable, and professional-grade code.

---

## 🤝 Contributing

Feel free to fork this repo and improve it — PRs welcome!