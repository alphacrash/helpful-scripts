import os

def find_empty_folders(directory):
    empty_folders = []
    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            empty_folders.append(root)
    return empty_folders
