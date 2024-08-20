import os

def find_and_delete_empty_folders(directory):
    empty_folders = []
    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            empty_folders.append(root)
    
    for folder in empty_folders:
        try:
            os.rmdir(folder)
            print(f"Deleted empty folder: {folder}")
        except OSError as e:
            print(f"Error deleting folder {folder}: {e}")
    
    return empty_folders