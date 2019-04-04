#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
#import the other messages 
#angular z and linear x matter

'''velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
vel_msg = Twist()

def travel(xdist):
    	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
        vel_msg.linear.x = 5
                
	ydist = 75
	
	t0 = rospy.Time.now().to_sec()
	current_distance = 0
        velocity_publisher.publish(vel_msg)
	while(current_distance < xdist):
	    velocity_publisher.publish(vel_msg)
	    t1 = rospy.Time.now().to_sec()
	    current_distance = 20* (t1-t0)
        vel_msg.linear.x = 0
	velocity_publisher.publish(vel_msg)
'''
def goToSpot(spotNumber):
	rospy.init_node('gridFollower', anonymous=True)
	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)	
	vel_msg = Twist()

	xdist = 28
	if spotNumber == 1:
		ydist = 50
		#do stuff
            
	elif spotNumber == 2:
            #travel(xdist)
                vel_msg.linear.y = 0
	        vel_msg.linear.z = 0
	        vel_msg.angular.x = 0
	        vel_msg.angular.y = 0
	        vel_msg.angular.z = 0
                vel_msg.linear.x = 4
                
	        ydist = 75
	        
	        t0 = rospy.Time.now().to_sec()
	        current_distance = 0
                velocity_publisher.publish(vel_msg)
	        while(current_distance < xdist):
	                velocity_publisher.publish(vel_msg)
	                t1 = rospy.Time.now().to_sec()
	                current_distance = 20* (t1-t0)
                vel_msg.linear.x = 0
	        velocity_publisher.publish(vel_msg)

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


                vel_msg.linear.x = 4
                t0 = rospy.Time.now().to_sec()
	        current_distance = 0
                velocity_publisher.publish(vel_msg)
	        while(current_distance < 20):
	                velocity_publisher.publish(vel_msg)
	                t1 = rospy.Time.now().to_sec()
	                current_distance = 20* (t1-t0)
                vel_msg.linear.x = 0
	        velocity_publisher.publish(vel_msg)

                
                #turn left
            #travel(ydist)

	elif spotNumber == 3:
		ydist = 50
		#do stuff
	elif spotNumber == 4:
		ydist = 75
		#do stuff

if __name__=='__main__':
	#init the node
	#rospy.init_node('gridFollower', anonymous=True)
	#setup the publisher here
	
	try:
		goToSpot(2)
	except rospy.ROSInterruptException:
		pass

	#build the message

	#send the message
