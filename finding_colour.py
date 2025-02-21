
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('data/robot_010.png', cv2.IMREAD_COLOR)

# Convert BGR to RGB for correct color representation
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create an empty image of the same shape
new_img = np.zeros_like(img)

# Define a mask to detect red shades
mask = (img[:, :, 0] > 100) & (img[:, :, 1] < 100) & (img[:, :, 2] < 100)

# Apply the mask to highlight red pixels in the new image
new_img[mask] = [255, 0, 0]  # Set detected red pixels to bright red

# Display the original and processed images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(new_img)
plt.title('Detected Red Areas')

plt.show()