#!/usr/bin/env python
import roslib
roslib.load_manifest('tutorialROSOpenCV')
import sys
import rospy
import cv
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time

height=str(640)
width=str(480)
capture=cv.CaptureFromCAM(0)

def callback(data):
    global height
    global width
    global capture
    string=str(data.data)
    b=string.split(' ')
    height=str(b[0])
    width=str(b[1])
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,int(width))
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,int(height))
    #global.fps=str(b[2])
    #print height+'\n'
    print str(height)
    print str(width)
    
    



def talker():
    #cv.NamedWindow("")
    global height
    global width
    #capture =cv.CaptureFromCAM(0)
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,int(width))
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,int(height))
    #cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FPS,2)
    #rate=cv.GetCaptureProperty(capture,cv.CV_CAP_PROP_FPS)
    #print rate
    bridge=CvBridge()
    pub = rospy.Publisher('chatter', Image)
    rospy.init_node('talker', anonymous=True)
    
    rospy.Subscriber("config", String, callback)
    r = rospy.Rate(30) # 10hz
    frames=0
    start_time=0
    check=0 
    while not rospy.is_shutdown():
        #str = "hello world %s"%rospy.get_time()
        frame=cv.QueryFrame(capture)
	if check==0:
		check=1
		start_time=time.time()

	frames=frames+1
	if frames%10==0:
		curtime=time.time()
		diff=curtime-start_time
		fps=frames/diff
		#print fps
        #ret,frame=capture.read()
        #image=np.asarray(frame[:,:])
	#a=image.shape
	#print a
        #rospy.loginfo(st)
        pub.publish(bridge.cv_to_imgmsg(frame, "bgr8"))
        #r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
