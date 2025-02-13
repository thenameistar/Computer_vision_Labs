import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Apply OpenCV's equalizeHist function
img_eq = cv2.equalizeHist(img)

# Create a new histogram for the equalized image
equalized_hist_data = np.zeros(256)
for i in range(img_eq.shape[0]):
    for j in range(img_eq.shape[1]):
        equalized_hist_data[int(img_eq[i,j])] += 1

# Create an array for the cumulative distribution function of the equalized image
equalized_cdf = equalized_hist_data.cumsum()

# Plot the original and equalized image along with their histograms and CDFs
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Show the original image
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Show the histogram of the original image
axs[0, 1].hist(img.flatten(), bins=256, range=[0, 256], cumulative=False)
axs[0, 1].set_title('Original Histogram')

# Show the equalized image from OpenCV
axs[1, 0].imshow(img_eq, cmap='gray')
axs[1, 0].set_title('Equalized Image (OpenCV)')
axs[1, 0].axis('off')

# Show the histogram of the equalized image from OpenCV
axs[1, 1].hist(img_eq.flatten(), bins=256, range=[0, 256], cumulative=False)
axs[1, 1].set_title('Equalized Histogram (OpenCV)')

plt.show()
