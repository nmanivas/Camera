#!/usr/bin/env python
import rospy
from axis_camera.msg import Axis
import random
import cv2
import cv
import roslib
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError

import numpy as np


def callback(ros_data):
    pub = rospy.Publisher('/chatter', Image)
    bridge=CvBridge()
    #print 'received image data of type:%s'% ros_data.format
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
    image_1=cv.fromarray(image_np)
    #print type(image_1)
    pub.publish(bridge.cv_to_imgmsg(image_1, "bgr8"))


def ptz():
    global image_1
     #rospy.init_node('axis_ptz_random_move')
      #  self.pub = rospy.Publisher('/cmd', Axis)
    pub = rospy.Publisher('/cmd', Axis)
    pub1 = rospy.Publisher('/chatter', Image)
    rospy.init_node('ptzcmd', anonymous=True)
    bridge=CvBridge()
    Message=Axis()
    sub=rospy.Subscriber('/image_raw/compressed', CompressedImage,callback,queue_size=1)
    r = rospy.Rate(40)
        
    while not rospy.is_shutdown():
        pan1=float(raw_input("Enter pan:"))
        tilt1=float(raw_input("Enter tilt:"))
        zoom1=float(raw_input("Enter zoom:"))
        brightness1=float(raw_input("Enter brightness:"))
        #auto=True
        Message.pan=pan1
        Message.tilt=tilt1
        Message.zoom=zoom1
        Message.brightness=brightness1
        #Message.autofocus=auto
        pub.publish(Message)
        r.sleep()

     #self.pub = rospy.Publisher('/cmd', Axis)

if __name__ == '__main__':
    try:
        ptz()
    except rospy.ROSInterruptException: pass


