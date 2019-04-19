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
        self.velocity_publisher.publish(self.vel_msg)
        while(current_distance < distance):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = 20 * (t1 - t0)
        self.vel_msg.linear.x = 0
        self.velocity_publisher.publish(self.vel_msg)

    def turn_left(self):
        self.vel_msg.angular.z = 14
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        self.velocity_publisher.publish(self.vel_msg)
        while(current_distance < 8):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = 20* (t1-t0)
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

    
    def turn_right(self):
        self.vel_msg.angular.z = -14
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        self.velocity_publisher.publish(self.vel_msg)
        while(current_distance < 8):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = 19* (t1-t0)
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

        
    def goto_parking_spot(self, spot_number):
        if (spot_number == 1):
            self.move_forward(25.5)
            self.turn_left()
            self.move_forward(15)
            self.turn_right()
            #now needs to return home
            self.turn_right()
            self.move_forward(15)
            self.turn_right()
            self.move_forward(25.5)
            self.turn_left()
            self.turn_left()
            #end of return home code --- has not been tested yet
        elif (spot_number == 2):
            self.move_forward(25.5)
            self.turn_left()
            self.move_forward(15)
            self.turn_left()

        elif (spot_number == 3):
            self.move_forward(25.5)
            self.turn_left()
            self.move_forward(29)
            self.turn_right()
        elif (spot_number == 4):
            self.move_forward(25.5)
            self.turn_left()
            self.move_forward(29)
            self.turn_left()


if __name__=='__main__':
    lf = LotFollower()
    lf.goto_parking_spot(1)
