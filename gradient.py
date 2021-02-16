import cv2 as cv
import numpy as np

img = cv.imread('/home/joshi-mukul/Downloads/cat.jpg')
cv.imshow('Cats',img)

#gradients and edges are different from mathemtical point of view.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#Laplacian return pencil shade like version
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel  computes gradient in x and y direction and computes in both
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('combined Sobel',combined_sobel)

#canny image detector 'multi stage process more advanced multi staged' 
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny',canny)


cv.waitKey(0)


