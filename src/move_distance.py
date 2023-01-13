#!/usr/bin/env python3

import rospy					#import the python library for ROS
from geometry_msgs.msg import Twist		#import the twist message from the std_msgs package
from turtlesim.msg import Pose			#import the Pose message from the turtlesim package

#Handling command line arguments
import sys

robot_x = 0

def shutdown():
	
	rospy.loginfo("Stop TB3")
	pub.publish(Twist())			#default Twist() has linear.x of 0 and angular.z of 0
	rate.sleep()

# /turtle1/Pose topic callback
def pose_callback(pose):
	global robot_x
	rospy.loginfo("Robot X = %f\n", pose.x)
	robot_x = pose.x

# Function to move turtle: Linear and angular velocities, and distance are arguments
def move_turtle(lin_vel, ang_vel, distance):
	global pub
	global rate
	global robot_x	
	rospy.init_node('move_distance')	#Initiate a Node called 'move_distance'

	# The /turtle1/cmd_vel is the topic in which we have to send Twist messages
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)	#Create a Publisher object
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback) #Creating new subscriber: Topic name = /turtle1/pose: Callback name: pose_callback

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

		#rospy.loginfo("Linear Vel = %f: Angular Vel = %f", lin_vel, ang_vel)

		# Checking the robot distance is greater than the desired distance
		# If it is greater, stop the node
		if(robot_x >= distance):
			rospy.loginfo("Robot Reached Destination")
			rospy.logwarn("Stopping Robot")
			#shutdown()
			break

		pub.publish(vel)
		rate.sleep()

if __name__== '__main__':
	try:
		# Providing linear and angular velocity through command line
		move_turtle(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))

	except rospy.ROSInterruptException:
		pass



