#!/usr/bin/env python3
# inverse kinematics example 
# remember to enable actuators in the GUI program first

import rospy					#import the python library for ROS
from open_manipulator_msgs.msg import JointPosition	#import JointPosition message from the open_manipulator_msgs package
from open_manipulator_msgs.srv import SetJointPosition
from open_manipulator_msgs.msg import KinematicsPose
from open_manipulator_msgs.srv import SetKinematicsPose
from geometry_msgs.msg import Pose
import math
from pyfirmata import Arduino, util
import time


board = Arduino('/dev/ttyACM1')

it = util.Iterator(board)
it.start()

# change to the correct pin number
light = board.get_pin('a:0:i')
temperature = board.get_pin('a:5:i')
button = board.get_pin('d:7:i')

def arm_forward():		#arm point forward; gripper open
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_kinematics_position = rospy.ServiceProxy('/goal_joint_space_path_to_kinematics_position', SetKinematicsPose)
	set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
	
	kinematics_pose = KinematicsPose()
	kinematics_pose.pose.position.x = 0.24
	kinematics_pose.pose.position.y = 0.01
	kinematics_pose.pose.position.z = 0.17
	resp1 = set_kinematics_position('planning_group', 'gripper', kinematics_pose, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)

	rospy.sleep(3)

def arm_left():			#arm point left; gripper close
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_kinematics_position = rospy.ServiceProxy('/goal_joint_space_path_to_kinematics_position', SetKinematicsPose)
	set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)

	kinematics_pose = KinematicsPose()
	kinematics_pose.pose.position.x = 0.01
	kinematics_pose.pose.position.y = 0.24
	kinematics_pose.pose.position.z = 0.17
	resp1 = set_kinematics_position('planning_group', 'gripper', kinematics_pose, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [-0.01]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)
	
	rospy.sleep(3)

def arm_home():			#arm point left; gripper close
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'
	set_kinematics_position = rospy.ServiceProxy('/goal_joint_space_path_to_kinematics_position', SetKinematicsPose)
	set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)

	kinematics_pose = KinematicsPose()
	kinematics_pose.pose.position.x = 0.15
	kinematics_pose.pose.position.y = 0.01
	kinematics_pose.pose.position.z = 0.2
	resp1 = set_kinematics_position('planning_group', 'gripper', kinematics_pose, 3)

	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [0.0]	# -0.01 for fully close and 0.01 for fully open
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
