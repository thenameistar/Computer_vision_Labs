import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram using OpenCV
hist_data = cv2.calcHist([img], [0], None, [256], [0,256])

# Create the plot
fig, axs = plt.subplots(1, 2)
axs[0].imshow(img, cmap='gray')
axs[0].axis('off')

# Use matplotlib to plot the histogram
axs[1].hist(img.ravel(), bins=256, range=[0,256], cumulative=True, histtype='step')

plt.show()
