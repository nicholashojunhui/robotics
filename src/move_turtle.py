#!/usr/bin/env python

import rospy					#import the python library for ROS
from geometry_msgs.msg import Twist		#import the twist message from the std_msgs package

#Handling command line arguments
import sys

def shutdown():
	
	rospy.loginfo("Stop TB3")
	pub.publish(Twist())			#default Twist() has linear.x of 0 and angular.z of 0
	rate.sleep()

# Function to move turtle: Linear and angular velocities are arguments
def move_turtle(lin_vel, ang_vel):
	global pub
	global rate	
	rospy.init_node('move_turtle')	#Initiate a Node called 'move_turtle'

	# The /turtle1/cmd_vel is the topic in which we have to send Twist messages
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)	#Create a Publisher object
	vel = Twist()				#Create a var named "vel" of type Twist
	rate = rospy.Rate(10)			#Set a publish rate of 10 Hz

	rospy.on_shutdown(shutdown)

	while not rospy.is_shutdown():
		
		# Adding linear and angular velocity to the message		
		vel.linear.x = lin_vel
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = ang_vel

		rospy.loginfo("Linear Vel = %f: Angular Vel = %f", lin_vel, ang_vel)

		pub.publish(vel)
		rate.sleep()

if __name__== '__main__':
	try:
		# Providing linear and angular velocity through command line
		move_turtle(float(sys.argv[1]),float(sys.argv[2]))

	except rospy.ROSInterruptException:
		pass



