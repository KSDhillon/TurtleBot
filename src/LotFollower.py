#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class LotFollower():
    def __init__(self):
        rospy.init_node('lotFollower', anonymous=True)
        self.vel_msg = Twist()
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)

        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.vel_msg.linear.x = 0

    def move_forward(self, distance):
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        self.vel_msg.linear.x = 4
        self.velocity_publisher.publish(vel_msg)
        while(current_distance < distance):
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = 20 * (t1 - t0)
        self.vel_msg.linear.x = 0
        self.velocity_publisher.publish(vel_msg)

    def turn_left(self):
        vel_msg.angular.z = 10
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        velocity_publisher.publish(vel_msg)
        while(current_distance < 8):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = 20* (t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    def goto_parking_spot(self, spot_number):
        if (spot_number == 2):
            self.move_forward(28)
            self.turn_left()
            self.move_forward(20)



if __name__=='__main__':
    lf = LotFollower()
    try:
        lf.goto_parking_spot(2)
    except rospy.ROSInterruptException:
        pass
