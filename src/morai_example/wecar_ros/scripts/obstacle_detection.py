#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float64,Bool,Float64MultiArray,Int16
from sensor_msgs.msg import LaserScan,PointCloud
from math import cos,sin,pi
from geometry_msgs.msg import Point32

class Obstacle_Detecting :

    def __init__(self):
        
        self.range_array = []
        self.is_person = 0
        rospy.init_node('lidar_parser', anonymous=True)
        rospy.Subscriber("/lidar2D", LaserScan, self.laser_callback)
        rospy.Subscriber("/pub_Isperson",Int16,self.Is_Person)    

        self.pcd_pub = rospy.Publisher('/lidar_Obstacle',Float64MultiArray, queue_size=1)
        self.dynamic_pub = rospy.Publisher('/dynamic_Obstacle',Float64MultiArray, queue_size=1)

        rate = rospy.Rate(30) # 30hz

        while not rospy.is_shutdown():
            static_Obstacle = self.static_Obstacle()
            dynamic_Obstacle = self.dynamic_Obstacle()

            self.dynamic_pub.publish(dynamic_Obstacle)
            self.pcd_pub.publish(static_Obstacle)

            rate.sleep()
        
    def laser_callback(self,msg):
        pcd=PointCloud()
        motor_msg=Float64()
        pcd.header.frame_id=msg.header.frame_id
        angle=0
        count = 0
        self.range_array = [None] * 360
        for r in msg.ranges :
            self.range_array[count] = r
            count += 1
            

    def static_Obstacle(self):
        count = 0
        self.array = [0,0,0]
        for r in self.range_array:
            if(self.is_person == 0):
                if(160<= count <= 190 and r<1.2):   # 
                    self.array[0] = 1
                if(80<= count <= 280 and r<1.2):    # 
                    self.array[1] = 1
                if(93<= count <= 160 and r<1.2):    # 
                    self.array[2] = 1
            count+=1
        self.is_Obstacle = Float64MultiArray(data = self.array)
        # print("static : " , self.is_Obstacle)
        return self.is_Obstacle


    def dynamic_Obstacle(self): # 
        self.dynamic_decision = [0,0]
        count = 0
        for r in self.range_array:
            if(90<= count <= 270 and r<1.2):   # 
                self.dynamic_decision[0] = 1
            if(163<= count <= 242 and r<0.8):    #  
                self.dynamic_decision[1] = 1
            count+=1
        self.is_dynamicObstacle = Float64MultiArray(data = self.dynamic_decision)
        print("dynamic : " , self.is_dynamicObstacle)
        return self.is_dynamicObstacle
    
    def Is_Person(self,msg):
        self.is_person=msg.data




if __name__ == '__main__':
    try:
        test=Obstacle_Detecting()
        
    except rospy.ROSInterruptException:
        pass



