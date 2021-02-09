#!/usr/bin/env python
# Foward kinematics example

import rospy					#import the python library for ROS
from open_manipulator_msgs.msg import JointPosition	#import JointPosition message from the open_manipulator_msgs package
from open_manipulator_msgs.srv import SetJointPosition
from geometry_msgs.msg import Pose
import math
from pyfirmata import Arduino, util
import time


board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

# change to the correct pin number
light = board.get_pin('a:0:i')
temperature = board.get_pin('a:5:i')
button = board.get_pin('d:7:i')

def arm_forward():		#arm point forward; gripper open
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_joint_position = rospy.ServiceProxy('/open_manipulator/goal_joint_space_path', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/open_manipulator/goal_tool_control', SetJointPosition)
	
	joint_position = JointPosition()
	joint_position.joint_name = ['joint1','joint2','joint3','joint4']
	joint_position.position =  [0, 0, 0, 0]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)

	rospy.sleep(3)

def arm_left():			#arm point left; gripper close
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_joint_position = rospy.ServiceProxy('/open_manipulator/goal_joint_space_path', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/open_manipulator/goal_tool_control', SetJointPosition)

	joint_position = JointPosition()
	joint_position.joint_name = ['joint1','joint2','joint3','joint4']
	joint_position.position =  [1.571, 0, 0, 0]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)
	
	rospy.sleep(3)

def arm_home():			#arm point left; gripper half close
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_joint_position = rospy.ServiceProxy('/open_manipulator/goal_joint_space_path', SetJointPosition)
        set_gripper_position = rospy.ServiceProxy('/open_manipulator/goal_tool_control', SetJointPosition)

	joint_position = JointPosition()
	joint_position.joint_name = ['joint1','joint2','joint3','joint4']
	joint_position.position =  [0, -1.052, 0.377, 0.709]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [0.00]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)
	
	rospy.sleep(3)

def blink():
    	board.digital[13].write(1)
    	time.sleep(1)
   	board.digital[13].write(0)

def talker():
	
	while True:

		#read values/status
    		brightness = light.read()
    		t = temperature.read()
    		bs = button.read()


    		#adjust and calibrate values
    		if brightness == None:
    			continue
    		else:
    			brightness = (brightness*1000)

    		if t == None:
    			continue
    		else:
    			temp = (t*1000)/2.048

    		#fufilling required conditions
    		if  temp > 32 and brightness < 25 and bs == True:
			blink()
			arm_home()

    		elif temp > 32 or brightness < 25 or bs == True:
			board.digital[13].write(1)
			arm_left()

    		else:
			board.digital[13].write(0)
			arm_forward()

    		print('Light: ',brightness)
    		print('Temp (degree C): ',temp)
    		print('Button status: ',bs)

    		time.sleep(1)


if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
