import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image and convert to grayscale
img = cv2.imread('data/coins.png')  # Ensure this image exists in your data folder
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image for visualization
output_img = img.copy()

# Loop through each contour and compute properties
for cnt in contours:
    # Bounding box
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Rotated bounding box
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(output_img, [box], 0, (0, 0, 255), 2)

    # Compute contour properties
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    
    # Convex Hull
    hull = cv2.convexHull(cnt)
    cv2.drawContours(output_img, [hull], 0, (255, 255, 0), 2)

    # Minimum enclosing circle
    (circle_x, circle_y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(circle_x), int(circle_y))
    radius = int(radius)
    cv2.circle(output_img, center, radius, (255, 0, 255), 2)

    # Moments to find centroid
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.circle(output_img, (cx, cy), 5, (0, 255, 255), -1)

# Display results
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
axs[0].set_title("Thresholded Image")
axs[0].axis("off")

axs[1].imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
axs[1].set_title("Contours & Properties")
axs[1].axis("off")

plt.show()
