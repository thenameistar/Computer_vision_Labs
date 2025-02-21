import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('data/robot_010.png', cv2.IMREAD_GRAYSCALE)

# Define Sobel Kernels
sobel_x = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

# Apply Sobel filters
sobel_x_result = cv2.filter2D(img, -1, sobel_x)
sobel_y_result = cv2.filter2D(img, -1, sobel_y)

# Calculate magnitude and direction
magnitude = np.sqrt(sobel_x_result**2 + sobel_y_result**2)
direction = np.arctan2(sobel_y_result, sobel_x_result)

# Show results
fig, axs = plt.subplots(1, 3)

# Display original image
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

# Display magnitude image
axs[1].imshow(magnitude, cmap='gray')
axs[1].set_title('Magnitude')
axs[1].axis('off')

# Display direction image
axs[2].imshow(direction, cmap='gray')
axs[2].set_title('Direction')
axs[2].axis('off')

plt.show()

