#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
n = 4


def main():

    pub = rospy.Publisher('mattias', UInt16, queue_size=20)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20)
    k = 1
    while not rospy.is_shutdown():
        rospy.loginfo(k)
        pub.publish(k)
        k += n
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
