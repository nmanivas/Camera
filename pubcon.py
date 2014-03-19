#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('config', String)
    rospy.init_node('pubcon', anonymous=True)
    #a=str(0)
    #r = rospy.Rate(10) # 10hz
    cam0=str(0)
    cam1=str(0)
    cam2=str(0)
    cam3=str(0)
    cam4=str(0)
    while not rospy.is_shutdown():
        cam0=0
        cam1=0
        cam2=0
        cam3=0
        cam4=0
        CameraNo=input("Enter the camera number:")
        height= input("Enter the image height:")
        width=input("Enter the image width:")
        fps=input("Enter the frame rate:")
        if CameraNo==0:
            cam0=1
        if CameraNo==1:
            cam1=1
        if CameraNo==2:
            cam2=1
        if CameraNo==3:
            cam3=1
        if CameraNo==4:
            cam4=1
        string =str(cam0)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(fps)+","+str(width)+","+str(height)
        print string
        #rospy.loginfo(str)
        pub.publish(string)
        #r.sleep(g

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
