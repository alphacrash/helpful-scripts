import os

def delete_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in extensions:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")