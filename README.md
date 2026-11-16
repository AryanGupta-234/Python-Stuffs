# Python Stuffs

A collection of small Python command-line utilities written while learning the language.

## What it does

- **`file content searcher.py`**: asks for a folder and a piece of text, reads every `.py` and `.pyw` file under that folder, and lists the files that contain the text. It warns when there are 15 or more matches.
- **`files structure app.py`**: asks for a folder and sorts the files inside it (including sub-folders) into `Images`, `Document`, `office 365 files` and `Python` folders by file extension.

## Built with

- Python 3 (standard library: `os`, `shutil`)
- `termcolor` for coloured terminal output
- `pandas` (imported by the file searcher)

## Run it

1. Install Python 3 and the dependencies:

       pip install termcolor pandas

2. Run either script from a terminal and answer the prompts:

       python "file content searcher.py"
       python "files structure app.py"

`files structure app.py` **moves** files rather than copying them, and keeps asking for another folder until you stop it with Ctrl+C. Try it on a copy of a folder first.

## Project status

Early learning project.

---

Part of [Aryan Gupta's projects](https://github.com/AryanGupta-234). Building [NOBAD](https://nobad-platform.aassworld99.workers.dev/): software with a point of view.
