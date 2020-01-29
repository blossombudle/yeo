#!/usr/bin/env python3


import ros
import sys
import rospy
#import tf
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 

import time
import math




class AutoDrive:
	def __init__(self):
		rospy.init_node('someone',anonymous=True)
		rospy.Subscriber("/scan", LaserScan, self.callback, queue_size=1)
		self.pub = rospy.Publisher('/motor', String, queue_size=1)

		#self.init_x, self.init_y = self.getPosition()

				
	
	@staticmethod
	def RAD2DEG(x):
		return ((x)*180/3.14159265358979323846)
	
	@staticmethod
	def isTooClose(distance):
		ret = distance == math.inf
		#print("[isTooClose] distance: {}, return value: {}".format(distance, ret))
		return ret
	
	@staticmethod
	def isClear(distance):
		Threshold = 0.3
		return distance >= Threshold and not AutoDrive.isTooClose(distance)


	def getPosition(self): #save by tuple
		'''
		while not rospy.is_shutdown():
			try:
				(trans,rot) = listener.lookupTransform("/map", "/base_footprint", rospy.Time(0))
				break

			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				continue
		x, y, z = trans
		return x, y
		'''
		pass
		

	def callback(self, scan):
		#result = Twist()
		#result.linear.x = 1
		#listener = tf.TransformListener()
		
		data = String()
		frontClear = False
		rightClear = False
		leftClear = False

		frontCloseCount = 0
		rightCloseCount = 0
		leftCloseCount = 0

		angleRange = 7

		frontAngle = 0
		rightAngle = 90
		leftAngle = -90


		for i, distance in enumerate(scan.ranges):
			angle = AutoDrive.RAD2DEG(scan.angle_min + scan.angle_increment * i)
			#print("angle: {}".format(angle))
			if frontAngle - angleRange <= angle <= frontAngle + angleRange:
				if AutoDrive.isTooClose(distance):
					frontCloseCount += 1
				elif AutoDrive.isClear(distance):
					frontClear = True

			elif rightAngle - angleRange <= angle <= rightAngle + angleRange:
				if AutoDrive.isTooClose(distance):
					rightCloseCount += 1
				elif AutoDrive.isClear(distance):
					rightClear = True

			elif leftAngle - angleRange <= angle <= leftAngle + angleRange:
				if AutoDrive.isTooClose(distance):
					leftCloseCount += 1
				elif AutoDrive.isClear(distance):
					leftClear = True


		tooCloseThreshold = 10

		frontTooClose = not frontClear and frontCloseCount >= tooCloseThreshold 
		rightTooClose = not rightClear and rightCloseCount >= tooCloseThreshold
		leftTooClose = not leftClear and leftCloseCount >= tooCloseThreshold

		print("===========================")
		print("frontClear : ", frontClear)
		print("rightClear : ", rightClear)
		print("leftClear : ", leftClear)

		print("frontTooClose : ", frontTooClose)
		print("rightTooClose : ", rightTooClose)
		print("leftTooClose : ", leftTooClose)
		print("===========================")

		
		# Front is Clear && Left is Wall
		if frontClear and not leftClear:
			if  not leftTooClose:		
				data = "F"	
			else:
				data = "FL"

		# Front is Clear && Left is Clear
		elif frontClear and leftClear:
			data = "FR"
			
		# Front is BLOCKED!!!
		elif not frontClear:
			data = "L"
		else:
			data = "stop"

		# machine arrived
		#x, y = self.getPosition()
		#x_gap = self.init_x - x
		#y_gap = self.init_y - y
		#total_gap = x_gap + y_gap
		#if total_gap <= 0.5:
		#	data = stop

		
		rospy.loginfo(data)
		
		self.pub.publish("stop")
		self.pub.publish(data)
		time.sleep(0.05)




if __name__=='__main__':
	#listener = tf.TransformListener()

	ad = AutoDrive()
	rospy.spin()
