import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)
# create an array to store the results - one element for each possible grey value
hist_data = np.zeros(256)
# Iterate over the pixels in the image
# (i.e. the elements in the underlying array)
# and increment the correct cell in the histogram array
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist_data[img[i,j]] += 1
# Create an array big enough to hold the histogram image
# Ask yourself: why 100?
hist_img = np.zeros([100,256])
# Draw the histogram by setting the correct pixels
# Use python array slicing to do this, rather than
# graphics primitives such as drawing lines
for i in range(256):
    hist_img[0:100,i] = 255
    hist_img[90:100,i] = i
    hist_img[0:int(hist_data[i]/max(hist_data)*100),i] = 0
    fig,axs = plt.subplots(1,2)
    axs[0].imshow(img, cmap = 'gray')
    axs[0].axis('off')
    axs[1].imshow(hist_img, cmap = 'gray')
    axs[1].invert_yaxis()
plt.show()
cv2.waitKey()
