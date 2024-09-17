import os
import shutil

def move_corresponding_videos_in_folder(folder_path):
    """Check if corresponding videos exist for images in the given folder and move them to the same directory."""
    # Define possible video extensions
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']

    # Walk through all subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Check if the file is an image (you can add more image extensions if needed)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
                image_path = os.path.join(root, file)
                image_filename_lower = file.lower()

                # Iterate over possible video extensions
                for ext in video_extensions:
                    # Replace the image extension with the video extension
                    video_filename = os.path.splitext(image_filename_lower)[0] + ext
                    video_path = os.path.join(root, video_filename)

                    # Check if the video file exists
                    if os.path.exists(video_path):
                        print(f"Found corresponding video: {video_path}")

                        # Move the video to the same directory as the image
                        destination_path = os.path.join(root, video_filename)
                        shutil.move(video_path, destination_path)
                        print(f"Moved {video_filename} to {destination_path}")
                        break
                else:
                    print(f"No corresponding video found for {image_path}")
                
def convert_filenames_to_uppercase(folder_path):
    """Convert every file to uppercase inside the folder and its subdirectories."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Get the current file path
            current_path = os.path.join(root, file)
            
            # Convert the filename to uppercase
            new_filename = file.upper()
            new_path = os.path.join(root, new_filename)
            
            # Rename the file
            os.rename(current_path, new_path)
            print(f"Renamed {current_path} to {new_path}")