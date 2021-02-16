
import cv2 as cv

img = cv.imread('/home/joshi-mukul/Downloads/groupimage2.jpg')
cv.imshow('Person', img)

def rescaleFrame(frame, scale=0.75):
    #for images, video and live video

    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)
cv.imshow('Image Resized',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=3)
print(f'No of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)