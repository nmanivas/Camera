#!/usr/bin/env python
import rospy
from std_msgs.msg import String

height=str(50)
width=str(100)
fps=str(15)
def callback(data):
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    global height
    string=str(data.data)
    b=string.split(' ')
    height=str(b[0])
    #global.width=str(b[1])
    #global.fps=str(b[2])
    print height+'\n'
    
    
def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    print str(height)
    print str(width)
    print str(fps)
    rospy.init_node('subcon', anonymous=True)

    rospy.Subscriber("config", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
