#!/usr/bin/env python
import rospy
from axis_camera.msg import Axis
import random

# pan [0, 360] horizontal position
# tilt [-90, 10] vertical position 

rospy.init_node('axis_ptz_random_move')
pub = rospy.Publisher('/cmd', Axis)

class TestRandomMove:
    def __init__(self):
        rospy.init_node('axis_ptz_random_move')
        self.pub = rospy.Publisher('/cmd', Axis)
        a = Axis()
        self.pub.publish(a)
      
    # The zoom does not seem to work
    def test_zoom(self, z):
        print("Zooming %f " % z)
        a = Axis()
        #a.fields = Axis.SELECT_ZOOM
        a.zoom = z
        self.pub.publish(a)
  
    def test_pan_tilt(self, hpos, vpos):
        a = Axis()
        #a.fields = Axis.SELECT_PAN + Axis.SELECT_TILT
        a.pan = hpos # Horizontal position
        a.tilt = vpos # Vertical position
        print("Moving to %f %f " % (a.pan, a.tilt))
        self.pub.publish(a)

if __name__ == "__main__":
    m = TestRandomMove()

    rospy.sleep(2.0)

    # Zooming does not seem to work ...
    # m.test_zoom(0.0)
    # rospy.sleep(2.0)

    # m.test_zoom(100.0)
    # rospy.sleep(2.0)

    positions = [(0, 0), (180, 0), (225, 0), (135, 0), (180, 0), (180, -90), (180, 10), (180, 0)]
    for p in positions:
        m.test_pan_tilt(p[0], p[1])
        rospy.sleep(3.0)
