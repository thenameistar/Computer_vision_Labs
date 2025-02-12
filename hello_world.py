import cv2
import os


# Specify the folder containing images
folder_path = 'path/to/your/images/folder'
output_folder = 'path/to/save/thumbnails'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the files in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check if the file is an image
        img = cv2.imread(os.path.join(folder_path, filename))
        
        # Get the dimensions of the image
        h, w = img.shape[:2]
        
        # Find the scaling factor
        if h > w:
            scale = 250 / h
        else:
            scale = 250 / w
        
        # Resize the image while maintaining the aspect ratio
        resized_img = cv2.resize(img, (int(w * scale), int(h * scale)))
        
        # Save the resized image
        output_path = os.path.join(output_folder, f"thumbnail_{filename}")
        cv2.imwrite(output_path, resized_img)
