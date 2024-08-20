import os

def get_files_with_extension(directory, extension):
    files_with_extension = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext == extension:
                files_with_extension.append(os.path.join(root, file))
    return files_with_extension