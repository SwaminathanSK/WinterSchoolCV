# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:33:10 2023

@author: swami
"""

# Djikstra's Algorithm

import cv2 as cv
import numpy as np

def inRange(img,x,y):
    return x>=0 and x<img.shape[0] and y>=0 and y<img.shape[1]

image = cv.imread("processedmaze.png")

temp = image.copy()

blue = [255, 0, 0]
white = [255, 255, 255]
black = [0, 0, 0]
found = [0, 255, 255]

startXY = (335,139)
endXY = (226, 720)
temp[226, 720] = [255, 255, 255]

dic = {}
open_set = set([startXY])
closed_set = set([])
g = {}
parents = {}

g[startXY] = 0 

startX = startXY[0]
startY = startXY[1]
endX = endXY[0]
endY = endXY[1]

dic[(startX, startY)] = [0, [(startX, startY)]]
parents[startXY] = startXY


flag = 0

temp[(startX, startY)] = blue

while len(open_set) != 0:
    n = None
    
    for (i, j) in open_set:
        if n == None or g[(i, j)]< g[n]:
            n = (i, j)
    
    i = n[0]
    j = n[1]
    
    for (r,s) in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
        
        if inRange(temp,r+i,s+j):
            
            if ((r+i, s+j) not in open_set) and ((r+i, s+j) not in closed_set) and ((temp[i+r, j+s] != black).any()):
                open_set.add((r+i, s+j))
                temp[i+r, j+s] = blue
                parents[(r+i, s+j)] = (i, j)
                g[(r+i, j+s)] = g[(i, j)] + 1
                
            elif (temp[i+r, j+s] != black).any():
                if g[(r+i, s+j)]> g[(i, j)] + 1:
                    parents[(r+i, s+j)] = (i, j)
                    g[(r+i, j+s)] = g[(i, j)] + 1
                    
                    if (r+i, s+j) in closed_set:
                        closed_set.remove((r+i, s+j))
                        open_set.add((r+i, s+j))
                        
            if (i+r, j+s) == endXY:
                flag = 1
                break
            #cv.waitKey(1)
            #cv.imshow("Image", temp)
    open_set.remove(n)
    closed_set.add(n)
    if flag == 1:
        break

cv.waitKey(1)
count = 0
if flag == 1:
    reconst_path = []
    n = endXY
    while parents[n] != n:
        reconst_path.append(n)
        n = parents[n]

    reconst_path.append(startXY)
    reconst_path.reverse()
    
    for i in reconst_path:
        count += 1
        temp[i[0]][i[1]] = found
    
print(count)
cv.imshow("Image", temp)
cv.waitKey(0)
cv.destroyAllWindows()
    