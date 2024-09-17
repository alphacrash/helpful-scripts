import os
import re
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import pillow_heif

# Register HEIF plugin
pillow_heif.register_heif_opener()

def organize_photos_by_date_in_filename(folder_path):
    """Organize photos into year and month folders and move the photos inside them."""
    pattern = r'[_\-.](\d{4})(\d{2})(\d{2})[_\-.]'
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            match = re.search(pattern, file)
            if match:
                year = int(match.group(1))
                month = match.group(2)
                if year > 2000:
                    year_folder = os.path.join(folder_path, str(year))
                    month_folder = os.path.join(year_folder, month)
                    
                    # Create year and month folders if they don't exist
                    if not os.path.exists(year_folder):
                        os.makedirs(year_folder)
                    if not os.path.exists(month_folder):
                        os.makedirs(month_folder)
                    
                    # Move the file to the respective year and month folder
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(month_folder, file)
                    shutil.move(source_path, destination_path)
                    print(f"Moved {file} to {destination_path}")

def organize_photos_by_date_taken(folder_path):
    """Organize photos into year and month folders based on the Date Taken property."""
    
    def get_date_taken(image_path):
        """Extract the Date Taken property from an image."""
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    decoded = TAGS.get(tag, tag)
                    if decoded == 'DateTimeOriginal':
                        return value
        except Exception as e:
            print(f"Error reading {image_path}: {e}")
        return None

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            date_taken = get_date_taken(file_path)
            if date_taken:
                year, month, _ = date_taken.split()[0].split(':')
                year_folder = os.path.join(folder_path, year)
                month_folder = os.path.join(year_folder, month)
                
                # Create year and month folders if they don't exist
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                if not os.path.exists(month_folder):
                    os.makedirs(month_folder)
                
                # Move the file to the respective year and month folder
                destination_path = os.path.join(month_folder, file)
                shutil.move(file_path, destination_path)
                print(f"Moved {file} to {destination_path}")
            else:
                print(f"No Date Taken found for {file}")

def get_date_taken_from_heic(heic_path):
    """Extract the Date Taken property from a HEIC image using pillow-heif."""
    try:
        image = Image.open(heic_path)
        exif_data = image.getexif()
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                print(f"Tag: {decoded}, Value: {value}")
                if decoded == 'DateTime':
                    return value
    except Exception as e:
        print(f"Error reading {heic_path}: {e}")
    return None

def organize_heic_and_mp4_by_date_taken(folder_path):
    """Organize HEIC and corresponding MP4 files into year and month folders based on the Date Taken property."""
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.heic'):
                heic_path = os.path.join(root, file)
                date_taken = get_date_taken_from_heic(heic_path)
                if date_taken:
                    year, month, _ = date_taken.split()[0].split(':')
                    year_folder = os.path.join(folder_path, year)
                    month_folder = os.path.join(year_folder, month)
                    
                    # Create year and month folders if they don't exist
                    if not os.path.exists(year_folder):
                        os.makedirs(year_folder)
                    if not os.path.exists(month_folder):
                        os.makedirs(month_folder)
                    
                    # Move the HEIC file to the respective year and month folder
                    destination_path_heic = os.path.join(month_folder, file)
                    shutil.move(heic_path, destination_path_heic)
                    print(f"Moved {file} to {destination_path_heic}")
                    
                    # Move the corresponding MP4 file if it exists
                    mp4_file = file.replace('.HEIC', '.MP4').replace('.heic', '.mp4')
                    mp4_path = os.path.join(root, mp4_file)
                    if os.path.exists(mp4_path):
                        destination_path_mp4 = os.path.join(month_folder, mp4_file)
                        shutil.move(mp4_path, destination_path_mp4)
                        print(f"Moved {mp4_file} to {destination_path_mp4}")
                else:
                    print(f"No Date Taken found for {file}")