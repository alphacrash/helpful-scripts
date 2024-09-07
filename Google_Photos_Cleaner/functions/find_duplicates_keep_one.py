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
