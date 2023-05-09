#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import random as rnd
import numpy as np

def talker():
    pub = rospy.Publisher('toggle_msg', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rnd_float = np.float32(rnd.randint(0,1000))
        rospy.loginfo(rnd_float)
        pub.publish(rnd_float)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass