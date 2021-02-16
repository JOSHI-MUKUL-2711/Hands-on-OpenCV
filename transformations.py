import cv2 as cv
import numpy as np

img = cv.imread('/home/joshi-mukul/Downloads/boston.jpg')

cv.imshow('Boston',img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated',translated)

# Rotation

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('Rotated',rotated)

rotated_2 = rotate(rotated, -45)
cv.imshow('rot',rotated_2)


#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)


#flipping
flip = cv.flip(img, -1) #0 filp vertically
#1 flip horizontally
#-1 flip both vertically as well as horizontally
cv.imshow('flip',flip)

cv.waitKey(0)