import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('data/coins.png', cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, binary_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Create a structuring element (5x5 elliptical shape)
struct_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Apply erosion to separate touching objects
eroded = cv2.erode(binary_thresh, struct_element, iterations=1)

# Apply dilation to restore the object shape after erosion
dilated = cv2.dilate(eroded, struct_element, iterations=1)

# Display results
fig, axs = plt.subplots(1, 3, figsize=(10, 4))
axs[0].imshow(binary_thresh, cmap='gray')
axs[0].set_title('Original Threshold')
axs[0].axis('off')

axs[1].imshow(eroded, cmap='gray')
axs[1].set_title('Eroded Image')
axs[1].axis('off')

axs[2].imshow(dilated, cmap='gray')
axs[2].set_title('Dilated Image')
axs[2].axis('off')

plt.show()
