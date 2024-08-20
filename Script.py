import os
import shutil

def find_unique_extensions(directory):
    unique_extensions = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:
                unique_extensions.add(ext)
    return unique_extensions

def delete_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in extensions:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

def get_files_with_extension(directory, extension):
    files_with_extension = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext == extension:
                files_with_extension.append(os.path.join(root, file))
    return files_with_extension

def delete_folder_with_name(directory, folder_name):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == folder_name:
                folder_path = os.path.join(root, dir)
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")

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

def main():
    while True:
        directory_path = input("Enter the directory path (or press Enter to use default): ")
        if not directory_path:
            directory_path = r'C:\Users\SUD\Downloads\Images'
        
        print("Choose an action:")
        print("1. Find unique file extensions")
        print("2. Delete files with specific extensions")
        print("3. Get files with a specific extension")
        print("4. Delete a folder with a specific name")
        print("5. Find empty folders")
        print("6. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            unique_extensions = find_unique_extensions(directory_path)
            print("Unique file extensions:", unique_extensions)
        elif choice == '2':
            extensions_to_delete = input("Enter the extensions to delete (comma-separated): ").split(',')
            extensions_to_delete = [ext.strip() for ext in extensions_to_delete]
            delete_files_with_extensions(directory_path, extensions_to_delete)
        elif choice == '3':
            extension_to_find = input("Enter the extension to find: ").strip()
            files_with_extension = get_files_with_extension(directory_path, extension_to_find)
            print(f"Files with {extension_to_find} extension:", files_with_extension)
        elif choice == '4':
            folder_name_to_delete = input("Enter the folder name to delete: ").strip()
            delete_folder_with_name(directory_path, folder_name_to_delete)
        elif choice == '5':
            empty_folders = find_and_delete_empty_folders(directory_path)
            print("Empty folders:", empty_folders)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()