#!/usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node('y5_detect_objects')

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        print("Detect objects node is broadcasting...")
        rate.sleep()