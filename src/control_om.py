#!/usr/bin/env python
# works for actual OM ONLY!
# does not work for actual OM_with_TB3

import rospy					#import the python library for ROS
from open_manipulator_msgs.msg import JointPosition	#import JointPosition message from the open_manipulator_msgs package
from open_manipulator_msgs.srv import SetJointPosition
from sensor_msgs.msg import JointState
import math
import time

def callback(msg):				#define a function called 'callback' that receives a parameter named 'msg'
	print msg.name			
	print msg.position	

def talker():
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_joint_position = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
	
	while not rospy.is_shutdown():
		joint_position = JointPosition()
		joint_position.joint_name = ['joint1','joint2','joint3','joint4']
		joint_position.position =  [-0.5, 0, 0.5, -0.5]		# in radians
		resp1 = set_joint_position('planning_group',joint_position, 3)
		gripper_position = JointPosition()
		gripper_position.joint_name = ['gripper']
		gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
		respg2 = set_gripper_position('planning_group',gripper_position, 3)

		sub_joint_state = rospy.Subscriber('/joint_states', JointState, callback)

if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
