import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([19,64,52])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # contours
    contours, hierarchy = cv.findContours(mask, 1 ,2)
    contour = max(contours, key = cv.contourArea)

    x,y,w,h = cv.boundingRect(contour)

    rect = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cv.destroyAllWindows()
