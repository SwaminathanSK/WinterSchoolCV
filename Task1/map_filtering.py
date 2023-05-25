# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:21:23 2023

@author: swami
"""


# Importing the required libraries
import cv2 as cv
import numpy as np



# Reading the image
map_default = cv.imread("image.png", 0)

height, width = map_default.shape

for i in range(height):
    for j in range(width):
        if map_default[i][j] in (233, 208, 227):
            map_default[i][j] = 0

'''
for i in range(height):
    for j in range(width):
        if map_default[i][j] not in  range(240, 256):
            map_default[i][j] = 0
'''
#cv.imwrite("image_gray.png", map_default)

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

