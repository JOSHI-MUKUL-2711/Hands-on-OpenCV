import cv2 as cv

img = cv.imread('/home/joshi-mukul/Downloads/boston.jpg')

cv.imshow('boston',img)

#converting an image to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#how to blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


# Edge Cascade
canny = cv.Canny(blur, 125,125)
cv.imshow('Canny images',canny) 


# Dialating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dialted',dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)


#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped = img[50:400, 100:500]
cv.imshow('Cropped',cropped)

cv.waitKey(0)