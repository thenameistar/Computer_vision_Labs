import cv2
import numpy as np

min_red = 0
max_red = 255
min_green = 0
max_green = 255
min_blue = 0
max_blue = 255

has_changed = True

def sliderCallback(x):
    global min_red, max_red, min_green, max_green, min_blue, max_blue, has_changed

    # Update the global values depending on which slider is adjusted
    if x < 100:
        min_red = x
    elif x >= 100 and x < 200:
        max_red = x
    elif x >= 200 and x < 300:
        min_green = x - 200
    elif x >= 300 and x < 400:
        max_green = x - 200
    elif x >= 400 and x < 500:
        min_blue = x - 400
    elif x >= 500:
        max_blue = x - 500
    
    has_changed = True
    print(f"Min Red: {min_red}, Max Red: {max_red}")
    print(f"Min Green: {min_green}, Max Green: {max_green}")
    print(f"Min Blue: {min_blue}, Max Blue: {max_blue}")

# Load the image
img = cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
new_img = np.zeros(img.shape, np.uint8)

# Create window and trackbars
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
        # Process the image based on slider values
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if (min_red <= img[i, j, 0] <= max_red) and \
                   (min_green <= img[i, j, 1] <= max_green) and \
                   (min_blue <= img[i, j, 2] <= max_blue):
                    new_img[i, j] = img[i, j]  # Keep the pixel if it’s in range
                else:
                    new_img[i, j] = [0, 0, 0]  # Set pixel to black if it’s out of range

        # Show the image with the applied color range
        cv2.imshow('Tracker sample', new_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
