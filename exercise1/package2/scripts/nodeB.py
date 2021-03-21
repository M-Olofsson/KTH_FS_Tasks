#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16, Float32
q = 0.15


class Transmitter:

    def __init__(self, pub):
        self.pub = pub

    def callback(self, msg):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
        k = msg.data/q
        self.pub.publish(k)


def main():
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=20)
    transmitter = Transmitter(pub)
    rospy.init_node('nodeB', anonymous=True)
    rospy.Subscriber('mattias', UInt16, transmitter.callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
