# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:21:23 2023

@author: swami
"""


# Importing the required libraries
import cv2 as cv
import numpy as np

# Reading the Image, and Blurring it to remove noise
map_default = cv.imread("image.png")
map_default = cv.GaussianBlur(map_default, (5, 5), 0)

# I used a color picker software to get these colors that indicate patches of colors that do not contribute to the pathways
colors = [[227, 208, 233], [249,192,156], [224,247,254], [192,223,180], [237,234,232], [231,227,225], [181,218,168], [230,232,252]]
height, width = map_default.shape[:2]

# Final touches by converting the corresponding colors to black and also other miscellaneous colors with any value less than 230 to black
for i in range(height):
    for j in range(width):
        for color in colors:
            if (map_default[i][j] == color).all() or map_default[i][j][0] <= 230 or map_default[i][j][1] <= 230 or map_default[i][j][2] <= 230:
                map_default[i][j] = [0, 0, 0]

# Storing the image into another file
cv.imwrite("image_gray.png", map_default)

#Displaying the image
cv.imshow("Final Map", map_default)
cv.waitKey(0)
cv.destroyAllWindows()

