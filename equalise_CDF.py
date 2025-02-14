import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Create an array to store the histogram data
hist_data = np.zeros(256)

# Iterate over the pixels in the image to fill the histogram
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist_data[img[i,j]] += 1

# Calculate the cumulative distribution function (CDF)
cdf = hist_data.cumsum()

# Normalize the CDF to the range [0, 255]
cdf_normalized = cdf * float(255) / cdf[-1]

# Apply the transfer function to equalize the image
equalized_img = np.interp(img.flatten(), range(256), cdf_normalized).reshape(img.shape)

# Create a new histogram for the equalized image
equalized_hist_data = np.zeros(256)
for i in range(equalized_img.shape[0]):
    for j in range(equalized_img.shape[1]):
        equalized_hist_data[int(equalized_img[i,j])] += 1

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

# Show the equalized image
axs[1, 0].imshow(equalized_img, cmap='gray')
axs[1, 0].set_title('Equalized Image')
axs[1, 0].axis('off')

# Show the histogram of the equalized image
axs[1, 1].hist(equalized_img.flatten(), bins=256, range=[0, 256], cumulative=False)
axs[1, 1].set_title('Equalized Histogram')

plt.show()
