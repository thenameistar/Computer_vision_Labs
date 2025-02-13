import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Create an array to store the histogram data (256 values for each grayscale level)
hist_data = np.zeros(256)

# Iterate over the pixels and populate the histogram
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist_data[img[i, j]] += 1

# Create an array for the histogram image
hist_img = np.zeros([100, 256])

# Draw the histogram
for i in range(256):
    hist_img[0:100, i] = 255
    hist_img[90:100, i] = i
    hist_img[0:int(hist_data[i] / max(hist_data) * 100), i] = 0  # Normalize to fit in 100px

# Compute cumulative distribution function (CDF)
cdf = np.cumsum(hist_data)  # Cumulative sum of histogram values
cdf_normalized = (cdf / max(cdf)) * 100  # Normalize to match the histogram scale

# Create an array for the cumulative distribution graph
cdf_img = np.zeros([100, 256])

# Draw the cumulative frequency graph
for i in range(256):
    cdf_img[0:100, i] = 255
    cdf_img[90:100, i] = i
    cdf_img[0:int(cdf_normalized[i]), i] = 0  # Normalized cumulative frequency

# Display both graphs
fig, axs = plt.subplots(1, 3, figsize=(12, 4))  # Create subplots for image, histogram, and CDF

axs[0].imshow(img, cmap='gray')
axs[0].axis('off')
axs[0].set_title("Original Image")

axs[1].imshow(hist_img, cmap='gray')
axs[1].invert_yaxis()
axs[1].set_title("Histogram")

axs[2].imshow(cdf_img, cmap='gray')
axs[2].invert_yaxis()
axs[2].set_title("Cumulative frequency")

plt.show()
