import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)


#paint the iamge certain color
#blank[:] = 0,0,255
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green',blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250), color=(0,250,0),thickness=-1)
#cv.imshow('Green',blank)


#draw a ciclepyh
cv.circle(blank, (50,50),50,color=(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)

#draw a line
cv.line(blank,(0,0),(500,500),color=(250,0,0),thickness=3)
cv.imshow('Line',blank)

#Write text
cv.putText(blank,'Hello World  my name is Mukul',(0,100), cv.FONT_HERSHEY_TRIPLEX,0.7,(100,105,200),2)
cv.imshow('text',blank)


# img = cv.imread('/home/joshi-mukul/Downloads/cat.jpg')
# cv.imshow('Cat',img)

cv.waitKey(0)