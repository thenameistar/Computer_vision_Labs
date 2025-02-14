import cv2
import numpy as np

# Read the image (load a noisy image or add noise to an image)
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)

# Add some salt-and-pepper noise to the image for demonstration
noise_img = np.copy(img)
salt_pepper = np.random.randint(0, 256, (img.shape[0], img.shape[1]), dtype=np.uint8)
noise_img[salt_pepper < 50] = 0  # salt
noise_img[salt_pepper > 200] = 255  # pepper

# Apply the median filter with a 3x3 kernel
median_img = cv2.medianBlur(noise_img, 3)

# Display the original, noisy, and median-filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Noisy Image', noise_img)
cv2.imshow('Median Filtered Image', median_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
