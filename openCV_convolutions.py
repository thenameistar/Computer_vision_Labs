import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('data/robot_010.png', cv2.IMREAD_GRAYSCALE)

# Define Sobel Kernels
sobel_x = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

# Apply Sobel filters using OpenCV's filter2D function
sobel_x_result = cv2.filter2D(img, -1, sobel_x)
sobel_y_result = cv2.filter2D(img, -1, sobel_y)

# Display original and Sobel filtered images
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(sobel_x_result, cmap='gray')
axs[1].set_title('Sobel X')
axs[1].axis('off')

axs[2].imshow(sobel_y_result, cmap='gray')
axs[2].set_title('Sobel Y')
axs[2].axis('off')


plt.show()
