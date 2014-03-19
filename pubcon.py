#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('config', String)
    rospy.init_node('pubcon', anonymous=True)
    #r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        height= input("Enter the image height:")
        width=input("Enter the image width:")
        fps=input("Enter the frame rate:")
        string = str(height)+" "+str(width)+" "+str(fps)
        print string
        #rospy.loginfo(str)
        pub.publish(string)
        #r.sleep(g

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
