# -*- coding: utf-8 -*-
"""
Created on Thu May 25 18:28:15 2023

@author: swami
"""

import cv2 as cv
import numpy as np

image = cv.imread("image_gray.png")
image = cv.GaussianBlur(image, (5, 5), 0)

cv.imshow("Blurred Image", image)
cv.waitKey(0)
cv.destroyAllWindows()