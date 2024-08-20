import os

def find_empty_folders(directory):
    empty_folders = []
    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            empty_folders.append(root)
    return empty_folders

# Example usage
if __name__ == "__main__":
    directory_path = r'C:\Users\SUD\Downloads\Images\Data'
    empty_folders = find_empty_folders(directory_path)
    for folder in empty_folders:
        print(f"Empty folder: {folder}")