import cv
import cv2
import numpy as np
#import pickel
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(2)
capture1 = cv.CaptureFromCAM(3)

def repeat():
    frame = cv.QueryFrame(capture)
    frame1 = cv.QueryFrame(capture1)		
    #cv.ShowImage("w1", frame)
    img=np.asarray(frame[:,:])
    img1=np.asarray(frame1[:,:])
    both=np.hstack((img,img1))
    cv2.imshow('Combine',both)
    

while True:
    repeat()
    if cv.WaitKey(33)==27:
        break

cv.DestroyAllWindows()


