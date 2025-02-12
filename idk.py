import cv2
import numpy as np
new_img = np.zeros((500, 500, 3), np.uint8)
# Create a BGR image (value of each channel is 0 to 255)
new_img[100:200, 100:200,0] = 128
new_img[150:250, 150:250,1] = 128
new_img[200:300, 200:300,2] = 128
new_img[300:400, 300:400, 0:3] = 192
cv2.imshow('RGB image', new_img)
# Create an 8-bit grey scale image (brightness from 0 to 255)
new_img2 = np.zeros((500, 500, 1), np.uint8)
new_img2[200:300, 200:300] = 128
cv2.imshow('Int greyscale image', new_img2)
# Create a float grey scale image (brightness from 0.0 to 1.0)
new_img3 = np.zeros((500, 500, 1), np.float32)
new_img3[200:300, 200:300] = 0.5
cv2.imshow('Float greyscale image', new_img3)
cv2.waitKey()