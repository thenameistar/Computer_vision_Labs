import numpy as np
import cv2

# Create a white canvas
image = np.ones((500, 500, 3), dtype="uint8") * 255  # White background

# Draw some shapes (e.g., circles for Olympic rings)
cv2.circle(image, (125, 125), 100, (255, 0, 0), 10)  # Blue ring
cv2.circle(image, (375, 125), 100, (0, 255, 0), 10)  # Green ring
cv2.circle(image, (250, 250), 100, (0, 0, 255), 10)  # Red ring
cv2.circle(image, (125, 375), 100, (0, 255, 255), 10)  # Yellow ring
cv2.circle(image, (375, 375), 100, (255, 255, 0), 10)  # Light blue ring

# Save the image
cv2.imwrite('olympic_rings.png', image)

# Show the image
cv2.imshow('Olympic Rings', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
