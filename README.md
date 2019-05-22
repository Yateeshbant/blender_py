import cv2 as cv
import numpy as np

mat=cv.imread("/content/TEST.bmp")

mat=cv.cvtColor(mat,cv.COLOR_RGB2GRAY)
vertices=[]
faces=[]
for i in range(mat.shape[0]):
  for j in range(mat.shape[1]):
    vertices.append([mat[i][j]/100,i/100,j/100])
for i in range(mat.shape[0]):
  for j in range(mat.shape[1]):
    faces
    
