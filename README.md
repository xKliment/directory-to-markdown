# Directory to Markdown Converter 📁➡️📝

This program allows you to create a Markdown file that describes the structure of a directory. It's a useful tool for documenting the contents of large directories and sharing this information in a readable format. 

## Features ✨

- Convert a directory structure to Markdown
- Option to save the Markdown file in the current directory or a directory of your choice
- Both GUI and console versions available
- Links in the Markdown file are relative, allowing you to navigate your file system directly from the Markdown file

## Usage 🚀

### GUI Version

1. Run `main-guy.pyw`
2. Use the "Browse" button to select the directory you want to document
3. Click "Save Here" to save the Markdown file in the same directory as the script
4. Alternatively, click "Save To" to choose a location to save the Markdown file

### Console Version

1. Run `main.py`
2. When prompted, enter the directory you want to document
3. When prompted, enter the name of the output file (without the .md extension)
4. The Markdown file will be saved in the same directory as the script

## Requirements 🧰
This program is written in Python and uses the following libraries:
- os
- tkinter (for the GUI version)
