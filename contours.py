import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/coins.png')  # Add 'data/' to the path

if img is None:
    print("Error: Image not found or cannot be loaded.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Otsu's thresholding to create a binary image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)  # Green color for contours
# Display the results
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Original Image")
axs[0].axis("off")

axs[1].imshow(thresh, cmap="gray")
axs[1].set_title("Thresholded Image")
axs[1].axis("off")

axs[2].imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
axs[2].set_title("Contours")
axs[2].axis("off")

plt.show()
