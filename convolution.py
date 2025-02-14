import cv2
import numpy as np

# Read the image
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel (for example, a blur kernel)
kernel1 = np.array([[1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9]])

# Another kernel (sharpening)
kernel2 = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])

# Apply the kernel to the image using convolution
img_convolved1 = cv2.filter2D(img, -1, kernel1)  # Apply the first kernel (blur)
img_convolved2 = cv2.filter2D(img, -1, kernel2)  # Apply the second kernel (sharpen)

# Display the original and convolved images
cv2.imshow('Original Image', img)
cv2.imshow('Convolved Image - Kernel 1 (Blur)', img_convolved1)
cv2.imshow('Convolved Image - Kernel 2 (Sharpen)', img_convolved2)

cv2.waitKey(0)
cv2.destroyAllWindows()
