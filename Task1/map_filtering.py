# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:21:23 2023

@author: swami
"""


# Importing the required libraries
import cv2 as cv
import numpy as np

map_default = cv.imread("image.png")

colors = [[227, 208, 233], [249,192,156], [224,247,254], [192,223,180], [237,234,232], [231,227,225], [181,218,168], [230,232,252]]
height, width = map_default.shape[:2]

for i in range(height):
    for j in range(width):
        for color in colors:
            if (map_default[i][j] == color).all() or map_default[i][j][0] <= 230 or map_default[i][j][1] <= 230 or map_default[i][j][2] <= 230:
                map_default[i][j] = [0, 0, 0]

# Reading the image
# map_default = cv.cvtColor(map_default, cv.COLOR_BGR2GRAY)

colors2 = [[233, 233, 233], [208, 208, 208], [227, 227, 227]]

'''
for i in range(height):
    for j in range(width):
        for color in colors2:
            if (map_default[i][j] == color).all():
                map_default[i][j] = 0
'''

'''
for i in range(height):
    for j in range(width):
        if map_default[i][j] not in  range(240, 256):
            map_default[i][j] = 0
'''
cv.imwrite("image_gray.png", map_default)

#Displaying the image
cv.imshow("Final Map", map_default)
cv.waitKey(0)
cv.destroyAllWindows()

'''
RED = (0,0,255)
BLUE = (255,0,0)

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

# Grey on Map, Grass, Lake, Plateau
colors = [[237, 234, 232], [192, 223, 180], [249,192,156], [224, 247, 254]]

maze = cv.imread("image.png")

n, l = maze.shape[:2]
tempmaze = maze.copy()
for i in range(n):
    for j in range(l):
        for color in colors:
            if (maze[i][j] == color).all():
                tempmaze[i][j] = [255, 255, 255]
                for (r,s) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if inRange(maze, (r+i, s+j)):
                        tempmaze[r+i][s+j] =  [255, 255, 255]
                break
        tempmaze[i][j] = [0,0,0]


tempmaze = cv.resize(tempmaze,(int(l*0.5), int(n*0.5)), interpolation=cv.INTER_AREA)
n, l = tempmaze.shape[:2]
for i in range(n):
    for j in range(l):
        if tempmaze[i][j][0] > 127:
             tempmaze[i][j] = (255,255,255)
        else:
            tempmaze[i][j] = (0,0,0)
'''

