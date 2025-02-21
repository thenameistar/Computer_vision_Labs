import cv2
import numpy as np

# Initialize min/max values for R, G, and B
min_red, max_red = 0, 255
min_green, max_green = 0, 255
min_blue, max_blue = 0, 255
has_changed = True

def sliderCallback(x):
    global min_red, max_red, min_green, max_green, min_blue, max_blue, has_changed
    min_red = cv2.getTrackbarPos('Min Red', 'Tracker sample')
    max_red = cv2.getTrackbarPos('Max Red', 'Tracker sample')
    min_green = cv2.getTrackbarPos('Min Green', 'Tracker sample')
    max_green = cv2.getTrackbarPos('Max Green', 'Tracker sample')
    min_blue = cv2.getTrackbarPos('Min Blue', 'Tracker sample')
    max_blue = cv2.getTrackbarPos('Max Blue', 'Tracker sample')
    has_changed = True

# Read image
img = cv2.imread('data/robot_010.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
new_img = np.zeros(img.shape, np.uint8)

# Create window and sliders
cv2.namedWindow('Tracker sample', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('Min Red', 'Tracker sample', 0, 255, sliderCallback)
cv2.createTrackbar('Max Red', 'Tracker sample', 255, 255, sliderCallback)
cv2.createTrackbar('Min Green', 'Tracker sample', 0, 255, sliderCallback)
cv2.createTrackbar('Max Green', 'Tracker sample', 255, 255, sliderCallback)
cv2.createTrackbar('Min Blue', 'Tracker sample', 0, 255, sliderCallback)
cv2.createTrackbar('Max Blue', 'Tracker sample', 255, 255, sliderCallback)

while True:
    if has_changed:
        has_changed = False
        new_img = np.zeros(img.shape, np.uint8)
        
        # Iterate over all pixels
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                r, g, b = img[i, j]
                if min_red <= r <= max_red and min_green <= g <= max_green and min_blue <= b <= max_blue:
                    new_img[i, j] = img[i, j]  # Keep color
                else:
                    new_img[i, j] = [0, 0, 0]  # Set to black
        
        cv2.imshow('Tracker sample', new_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
