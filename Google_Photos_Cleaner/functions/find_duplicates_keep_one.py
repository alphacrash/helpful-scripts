import os
import hashlib

def hash_file(file_path):
    """Generate a hash for a given file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates_keep_one(directory):
    """Find and remove duplicate files in a directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in file_hashes:
                print(f"Duplicate found: {file_path} (duplicate of {file_hashes[file_hash]})")
                os.remove(file_path)
            else:
                file_hashes[file_hash] = file_path

def find_duplicates(directory1, directory2):
    """Find duplicate files across two directories."""
    file_hashes = {}
    duplicates = {}

    def traverse_directory(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                if file_hash in file_hashes:
                    if file_hash not in duplicates:
                        duplicates[file_hash] = [file_hashes[file_hash]]
                    duplicates[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    # Traverse both directories
    traverse_directory(directory1)
    traverse_directory(directory2)

    return duplicates

def find_duplicates_to_delete(source_directory, destination_directory):
    """Find duplicate files in the source directory that can be deleted."""
    file_hashes = {}
    duplicates_to_delete = []

    def traverse_directory(directory, is_source):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                if file_hash in file_hashes:
                    if is_source:
                        duplicates_to_delete.append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    # Traverse the destination directory first
    traverse_directory(destination_directory, is_source=False)
    # Traverse the source directory
    traverse_directory(source_directory, is_source=True)

    return duplicates_to_delete

def find_duplicates_to_delete_filename(source_directory, destination_directory, delete_duplicates="NO"):
    """Find duplicate files in the source directory that can be deleted based on file names."""
    file_names = {}
    duplicates_to_delete = []

    def traverse_directory(directory, is_source):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_lower = file.lower()
                if file_lower in file_names:
                    if is_source:
                        duplicates_to_delete.append(file_path)
                        if delete_duplicates == "YES":
                            os.remove(file_path)
                else:
                    file_names[file_lower] = file_path

    # Traverse the destination directory first
    traverse_directory(destination_directory, is_source=False)
    # Traverse the source directory
    traverse_directory(source_directory, is_source=True)

    return duplicates_to_delete
