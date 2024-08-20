import os

def find_unique_extensions(directory):
    unique_extensions = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:
                unique_extensions.add(ext)
    return unique_extensions