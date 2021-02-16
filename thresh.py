import cv2 as cv

img = cv.imread('/home/joshi-mukul/Downloads/cat1.jpeg')
cv.imshow('Cat1',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple Thresholding
Threshold, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# simple thresholding inv
Threshold, thresh_inv = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inv', thresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)
#also can use the gaussian method

cv.waitKey(0)

