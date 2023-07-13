import os
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files(startpath):
    markdown = "# Directory Structure of `{}`\n\n".format(startpath)
    startdir_name = os.path.basename(startpath)
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        folder_name = os.path.basename(root)
        folder_path = os.path.join(startdir_name, os.path.relpath(root, startpath))
        markdown += '{}- [{}](./{})\n'.format(indent, folder_name, folder_path.replace('\\', '/'))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file_path = os.path.join(folder_path, f)
            markdown += '{}- [{}](./{})\n'.format(subindent, f, file_path.replace('\\', '/'))
    return markdown

def browse_directory():
    directory = filedialog.askdirectory()
    directory_var.set(directory)

def save_markdown_here():
    directory = directory_var.get()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Please select a directory.")
        return
    filename = os.path.basename(directory) + '.md'
    markdown = list_files(directory)
    with open(filename, 'w') as f:
        f.write(markdown)
    messagebox.showinfo("Success", "The markdown file has been successfully saved in the current directory as '{}'.".format(filename))

def save_markdown_to():
    directory = directory_var.get()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Please select a directory.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".md")
    if not filename:
        return
    markdown = list_files(directory)
    with open(filename, 'w') as f:
        f.write(markdown)
    messagebox.showinfo("Success", "The markdown file has been successfully saved.")

root = tk.Tk()
root.title("Directory to Markdown")

directory_var = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Select a directory:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame, textvariable=directory_var, width=50)
entry.pack(side=tk.LEFT)

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.pack(side=tk.LEFT)

save_here_button = tk.Button(root, text="Save Here", command=save_markdown_here, padx=10, pady=5)
save_here_button.pack()

save_to_button = tk.Button(root, text="Save To", command=save_markdown_to, padx=10, pady=5)
save_to_button.pack()

root.mainloop()
