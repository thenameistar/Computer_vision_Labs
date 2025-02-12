import cv2
import numpy as np
import os

# Specify the folder and get image files
folder_path = 'data/'
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

# Check if there are 16 images
if len(image_files) != 16:
    print("Please make sure there are exactly 16 images in the folder.")
else:
    # Read images
    images = [cv2.imread(os.path.join(folder_path, f)) for f in image_files]

    # Resize images to 200x200 pixels
    resized_images = [cv2.resize(img, (200, 200)) for img in images]

    # Create an empty array for the mosaic
    mosaic = np.vstack([np.hstack(resized_images[i:i+4]) for i in range(0, 16, 4)])

    # Save and show the mosaic
    cv2.imwrite('mosaic_image.jpg', mosaic)
    cv2.imshow('Mosaic', mosaic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
