import cv2 as cv
import numpy as np

mat=cv.imread("/content/TEST.bmp")

mat=cv.cvtColor(mat,cv.COLOR_RGB2GRAY)
vertices=""
faces=""
for i in range(mat.shape[0]):
  for j in range(mat.shape[1]):
    vertices=vertices+str("v "+str(mat[i][j]/100)+str(i/100)+str(j/100)+"\n")
  
y=mat.shape[1]
for x in range(int(mat.shape[1]-1)):
    for i in range(mat.shape[0]-1):
        a=i +(x*y)
        b=i+1+(x*y)
        c=i+mat.shape[1]+(x*y)
        d=i+mat.shape[1]+1+(x*y)
        faces+=str("f "+str(a)+'//'+str(b)+" "+str(b)+"//"+str(d)+" "+str(d)+"//"+str(c)+" "+str(c)+"//"+str(a)+"\n")
