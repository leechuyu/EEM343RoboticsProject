#! /usr/bin/env python

import sys
import time
import copy 
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous = True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("sensor_arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)


#get current joint values for group sensor_arm
sensor_joint_variables = group.get_current_joint_values()


#begin sensing for 5s
sensor_joint_variables [0] = -0.6284
sensor_joint_variables [1] = 0.1772
sensor_joint_variables [2] = 0.2095
sensor_joint_variables [3] = 0
group.set_joint_value_target(sensor_joint_variables)

plan2 = group.plan()
group.go(wait=True)

sensor_joint_variables [0] = -0.6284
sensor_joint_variables [1] = 0.1772
sensor_joint_variables [2] = 0.2095
sensor_joint_variables [3] = 0.08
group.set_joint_value_target(sensor_joint_variables)

plan2 = group.plan()
group.go(wait=True)
time.sleep(10)

#sensor arm at initial position
sensor_joint_variables [0] = 0
sensor_joint_variables [1] = 0
sensor_joint_variables [2] = 0
sensor_joint_variables [3] = 0
group.set_joint_value_target(sensor_joint_variables)

plan2 = group.plan()
group.go(wait=True)

group = moveit_commander.MoveGroupCommander("water_arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

#get current joint values for group water_arm
water_joint_variables = group.get_current_joint_values()

#water arm at initial position

#water the left plant for 5s
water_joint_variables [0] = -0.8644
water_joint_variables [1] = -0.3061
water_joint_variables [2] = 0.8297
group.set_joint_value_target(water_joint_variables)

plan2 = group.plan()
group.go(wait=True)
time.sleep(10)

#water the right plant for 5s
water_joint_variables [0] = -0.3060
water_joint_variables [1] = -0.2094
water_joint_variables [2] = 1.5707
group.set_joint_value_target(water_joint_variables)

plan2 = group.plan()
group.go(wait=True)
time.sleep(10)

#return to initial position
water_joint_variables [0] = 0
water_joint_variables [1] = 0
water_joint_variables [2] = 0
group.set_joint_value_target(water_joint_variables)

plan2 = group.plan()
group.go(wait=True)


moveit_commander.roscpp_shutdown()

