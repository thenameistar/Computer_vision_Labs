import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read images
img1 = cv2.imread('data/test01.jpg')
img2 = cv2.imread('data/test01.jpg', cv2.IMREAD_GRAYSCALE)

# Create subplots
fig, axs = plt.subplots(nrows=1, ncols=2)

# Display original image
axs[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[0].title.set_text('Original Image')
axs[0].axis('off')

# Display grayscale image
axs[1].imshow(img2, cmap='gray')
axs[1].title.set_text('Greyscale Image')
axs[1].axis('off')

plt.show()
