import os

# Define the path to the directory
directory_path = r'D:\Music Videos'

# Traverse the directory
for root, dirs, files in os.walk(directory_path):
    # Print the folder name
    print(f"Folder: {root}")
    # Print the file names
    for file in files:
        print(f"  File: {file}")