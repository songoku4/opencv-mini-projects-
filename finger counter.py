import cv2
import time
import os
import trackingmodule as htm



wCam,hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success, img = cap.read()




    cv2.imshow("image", img)
    cv2.waitKey(1)

