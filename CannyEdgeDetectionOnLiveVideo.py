import cv2
import numpy as np

capture=cv2.VideoCapture(0)
while(True):
    rect,frame=capture.read()
    changed=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #define range of red color in HSV
    minval=np.array([30,150,50])
    maxval=np.array([255,255,180])
    #create a red HSV color boundary and threshold HSV model
    thresh=cv2.inRange(changed,minval,maxval)
    #Perform bitwise AND between thresh and captured image
    result=cv2.bitwise_and(frame,frame,mask=thresh)
    #find edges
    edges1=cv2.Canny(frame,100,150)
    cv2.imshow('Canny',edges1)
    key=cv2.waitKey(1)&0xff
    #press "esc" to close
    if key==27:
        break
capture.release()
cv2.destroyAllWindows()
