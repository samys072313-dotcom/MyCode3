import cv2
import time
import math


video = cv2.VideoCapture("C:/Users/rajka/Downloads/PRO-c116-Teacher-Reference-Code-main (1)/PRO-c116-Teacher-Reference-Code-main/bb3.mp4")
tracker = cv2.TrackerMIL_create()
returned,img=video.read()

bbox = cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)
print(bbox)
while True: 
    check,img = video.read()
    cv2.imshow("result",img)
    key = cv2.waitKey(0)
    if key==32:
        print("Stopped") 
        break

    video.release()
    cv2.destroyALLWindows()