import cv2 as cv
import numpy as np

img = cv.imread('/home/joshi-mukul/Downloads/boston.jpg')
cv.imshow('Boston',img)

b,g,r = cv.split(img)

# cv.imshow('Blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)


#another way

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue_',blue)
cv.imshow('green_',green)
cv.imshow('red_',red)
cv.waitKey(0)




