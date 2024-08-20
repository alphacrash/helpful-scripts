import os
import shutil

def delete_folder_with_name(directory, folder_name):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == folder_name:
                folder_path = os.path.join(root, dir)
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
