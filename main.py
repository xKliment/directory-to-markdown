import os

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

# ASCII Art
print("""                                                                                                                                                                          
 ____  _             _                  _          _____         _     _               
|    \|_|___ ___ ___| |_ ___ ___ _ _   | |_ ___   |     |___ ___| |_ _| |___ _ _ _ ___ 
|  |  | |  _| -_|  _|  _| . |  _| | |  |  _| . |  | | | | .'|  _| '_| . | . | | | |   |
|____/|_|_| |___|___|_| |___|_| |_  |  |_| |___|  |_|_|_|__,|_| |_,_|___|___|_____|_|_|
                                |___|
""")

while True:
    # ask for directory
    directory = input("\nEnter the directory (or 'quit' to stop): ")
    if directory.lower() == 'quit':
        break
    if not os.path.exists(directory):
        print("The directory does not exist. Please try again.")
        continue
    
    # ask for output file name
    filename = input("Enter the output filename (without .md extension): ")
    filename = filename.strip() + ".md"
    
    # ask for saving directory
    save_directory = input("Press Enter to save in the current directory or provide a directory to save to: ").strip()
    if save_directory and not os.path.exists(save_directory):
        print("The provided save directory does not exist. Please try again.")
        continue
    
    markdown = list_files(directory)
    
    save_path = filename if not save_directory else os.path.join(save_directory, filename)
    with open(save_path, 'w') as f:
        f.write(markdown)
    print("""
  _______                              __            __ 
 |   _   .-----.-----.-----.----.---.-|  |_.-----.--|  |
 |.  |___|  -__|     |  -__|   _|  _  |   _|  -__|  _  |
 |.  |   |_____|__|__|_____|__| |___._|____|_____|_____|
 |:  1   |                                              
 |::.. . |                                              
 `-------'
""")
    print("\nThe directory structure has been saved as '{}'.".format(filename))

print("\n Bye!")
