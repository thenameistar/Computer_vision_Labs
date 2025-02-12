import cv2
import os

# Specify the folder
folder_path = 'data/'
output_folder = 'thumbnails/'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all image files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        img = cv2.imread(os.path.join(folder_path, filename))
        
        # Resize the image
        height, width = img.shape[:2]
        max_dim = max(height, width)
        scale = 250 / max_dim  # Scale factor to make the largest dimension 250px
        new_size = (int(width * scale), int(height * scale))
        
        # Create the thumbnail
        thumbnail = cv2.resize(img, new_size)
        
        # Save the thumbnail with the original filename
        cv2.imwrite(os.path.join(output_folder, filename), thumbnail)

print("Thumbnails created successfully.")
