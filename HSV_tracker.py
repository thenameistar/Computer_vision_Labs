import cv2
import numpy as np

# Initialize min and max values for Hue, Saturation, and Value
minH, maxH = 0, 180
minS, maxS = 0, 255
minV, maxV = 0, 255

has_changed = True

# Callback function for trackbars
def sliderCallback(x):
    global has_changed
    has_changed = True

# Read the image and convert to HSV
img = cv2.imread('data/robot_010.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a window with trackbars
cv2.namedWindow('HSV Tracker')
cv2.createTrackbar('Hue Min', 'HSV Tracker', minH, 180, sliderCallback)
cv2.createTrackbar('Hue Max', 'HSV Tracker', maxH, 180, sliderCallback)
cv2.createTrackbar('Sat Min', 'HSV Tracker', minS, 255, sliderCallback)
cv2.createTrackbar('Sat Max', 'HSV Tracker', maxS, 255, sliderCallback)
cv2.createTrackbar('Val Min', 'HSV Tracker', minV, 255, sliderCallback)
cv2.createTrackbar('Val Max', 'HSV Tracker', maxV, 255, sliderCallback)

while True:
    if has_changed:
        has_changed = False
        
        # Get trackbar values
        minH = cv2.getTrackbarPos('Hue Min', 'HSV Tracker')
        maxH = cv2.getTrackbarPos('Hue Max', 'HSV Tracker')
        minS = cv2.getTrackbarPos('Sat Min', 'HSV Tracker')
        maxS = cv2.getTrackbarPos('Sat Max', 'HSV Tracker')
        minV = cv2.getTrackbarPos('Val Min', 'HSV Tracker')
        maxV = cv2.getTrackbarPos('Val Max', 'HSV Tracker')

        # Define lower and upper HSV range
        lower_bound = np.array([minH, minS, minV])
        upper_bound = np.array([maxH, maxS, maxV])

        # Create a mask to filter out the selected color range
        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)

        # Apply the mask to the original image
        result = cv2.bitwise_and(img, img, mask=mask)

        # Show the images
        cv2.imshow('Original', img)
        cv2.imshow('Masked Image', result)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
