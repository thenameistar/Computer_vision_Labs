import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('data/robot_010.png')

# Convert to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define two ranges for red (red wraps around 0 in HSV)
lower_red1 = np.array([0, 120, 70])     # First red range
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])   # Second red range
upper_red2 = np.array([180, 255, 255])

# Create masks for both red ranges
mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)

# Combine the two masks
mask = cv2.bitwise_or(mask1, mask2)

# Apply the mask
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Display results
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Original Image")
axs[0].axis("off")

axs[1].imshow(mask, cmap="gray")
axs[1].set_title("Mask")
axs[1].axis("off")

axs[2].imshow(cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB))
axs[2].set_title("Masked Image")
axs[2].axis("off")

plt.show()
