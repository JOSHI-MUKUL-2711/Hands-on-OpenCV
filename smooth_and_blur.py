import cv2 as cv

img = cv.imread('/home/joshi-mukul/Downloads/cat.jpg')
cv.imshow('Cat',img)

#averaging

average = cv.blur(img,(3,3)) #high the krenel size high high the blur
cv.imshow('Average Blur',average)

#gaussian blur    less effect the averaging but more nautral 

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur',gauss)

#meadian blur same as averaging (instead of find avg of surrounding pixels it find median of the surrounding pixels)
#more effective in reducing noise better then the both
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

#Bilateral blur
#most effective but retains the edges
bilateral = cv.bilateralFilter(img,5, 15,15)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)

