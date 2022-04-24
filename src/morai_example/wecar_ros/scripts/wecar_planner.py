#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os
import rospy
import rospkg
import numpy as np
import time
from nav_msgs.msg import Path,Odometry
from std_msgs.msg import Float64,Int16,Float32MultiArray,Bool,Float64MultiArray
from geometry_msgs.msg import PoseStamped,Point
from morai_msgs.msg import EgoVehicleStatus,CtrlCmd,GetTrafficLightStatus,SetTrafficLight #
from lib.utils import pathReader, findLocalPath,purePursuit,pidController,velocityPlanning,latticePlanner#
import tf
from math import cos,sin,sqrt,pow,atan2,pi


class wecar_planner():
    def __init__(self):
        rospy.init_node('wecar_planner', anonymous=True)

        arg = rospy.myargv(argv=sys.argv)
        self.path_name_1=arg[1]
        self.path_name_2=arg[2]
        self.path_name_3=arg[3]
        self.path_name_4=arg[4]
        path_count = 1
        time_count = 1
        goal = False # 1 
        global timer
        timer = 0
        self.lidarObstacle = [0,0]

        #publisher
        global_path_pub= rospy.Publisher('/global_path',Path, queue_size=1) ## global_path publisher
        local_path_pub= rospy.Publisher('/local_path',Path, queue_size=1) ## local_path publisher
        self.motor_pub = rospy.Publisher('commands/motor/speed',Float64, queue_size=1)
        self.servo_pub = rospy.Publisher('commands/servo/position',Float64, queue_size=1)
        path_count_pub = rospy.Publisher('/path_count', Int16, queue_size=1)
        waypoint_pub = rospy.Publisher('/current_waypoint', Int16, queue_size=1)
        ########################  lattice  ########################
        for i in range(1,8):            
            globals()['lattice_path_{}_pub'.format(i)]=rospy.Publisher('lattice_path_{}'.format(i),Path,queue_size=1)  
        ########################  lattice  ########################
        
        #subscriber
        rospy.Subscriber("/Ego_topic", EgoVehicleStatus, self.statusCB) ## Vehicl Status Subscriber 
        rospy.Subscriber("/lidar_Obstacle", Float64MultiArray, self.lidarObstacleInfoCB)
        rospy.Subscriber('/target_speed', Float64, self.speedCB)

        #def
        self.is_status=False ## 
        #self.is_obj=True ## 
        self.steering_angle_to_servo_offset=0.5304 ## servo moter offset
        self.rpm_gain = 4616
        self.motor_msg=Float64()
        self.servo_msg=Float64()
        

        #class
        path_reader=pathReader('wecar_ros') ## 
        pure_pursuit=purePursuit() ## purePursuit import
        pid=pidController() ## pidController import
        

        #read path
        self.global_path=path_reader.read_txt(self.path_name_1+".txt") ## 
        self.total_path=path_reader.read_txt(self.path_name_4+".txt") ##
        vel_planner=velocityPlanning(1, 0.15) ## 
        vel_profile=vel_planner.curveBasedVelocity(self.total_path,30)
        

        
        #time var
        count=0
        rate = rospy.Rate(30) # 30hz

        lattice_current_lane=3

        while not rospy.is_shutdown():
            
                        
            if self.is_status==True : #and self.is_obj==True: ## 
                ##
                local_path,self.current_waypoint=findLocalPath(self.global_path,self.status_msg) 
                


                ########################  lattice  ########################
                vehicle_status=[self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi,self.status_msg.velocity.x/3.6]
                #print("Out : " , self.is_status)
                lattice_path,selected_lane=latticePlanner(local_path,self.lidarObstacle,vehicle_status,lattice_current_lane)#(local_path,global_obj,vehicle_status,lattice_current_lane) 변경
            
                if path_count == 1 and 95 <= self.current_waypoint <= 163:
                    selected_lane = 3
                elif path_count == 2 and 122 <= self.current_waypoint <= 188:
                    selected_lane = 3
                lattice_current_lane=selected_lane
                             
                if selected_lane != -1: 
                    local_path=lattice_path[selected_lane]                
                
                if len(lattice_path)==7:                    
                    for i in range(1,8):
                        globals()['lattice_path_{}_pub'.format(i)].publish(lattice_path[i-1])
                ########################  lattice  ########################


                
                pure_pursuit.getPath(local_path) ## 
                pure_pursuit.getEgoStatus(self.status_msg) ##

                self.steering=pure_pursuit.steering_angle()
                
            

                self.servo_msg = self.steering*0.021 + self.steering_angle_to_servo_offset
                self.motor_msg = self.go_stop*vel_profile[self.current_waypoint]*self.rpm_gain /3.6 #
                                
                
    
                local_path_pub.publish(local_path) ## 

                self.servo_pub.publish(self.servo_msg)
                #self.motor_pub.publish(self.motor_msg)
                #self.print_info()
            
            if count==300 : ## 
                global_path_pub.publish(self.global_path)
                count=0
            count+=1
            
            if path_count == 1 and 45 <= self.current_waypoint <= 48: # 
                goal = True
            elif path_count == 1:
                goal = False

            if goal == True and time_count == 1: #
                init_time = time.time()
                time_count = 2
            elif goal == True and time_count == 2:
                timer = time.time() - init_time

            if goal == True and timer <= 5: # 
                self.motor_pub.publish(0)
            else:
                self.motor_pub.publish(self.motor_msg)

            #if path_count == 1 and self.current_waypoint == 327: # past_waypoint ver
            if path_count == 1 and self.current_waypoint == 333:
                self.global_path=path_reader.read_txt(self.path_name_2+".txt")
                path_count = 2

            if path_count == 2 and self.current_waypoint == 724:
                self.global_path=path_reader.read_txt(self.path_name_3+".txt")
                path_count = 3
            
            path_count_pub.publish(path_count)
            waypoint_pub.publish(self.current_waypoint)
            print(self.current_waypoint)
            rate.sleep()

    def lidarObstacleInfoCB(self,data):
        self.lidarObstacle = Float64MultiArray()
        self.lidarObstacle= data
    
    def speedCB(self, msg):
        self.go_stop = msg.data
      

    def statusCB(self,data): ## Vehicl Status Subscriber 
        self.status_msg=data
        br = tf.TransformBroadcaster()
        br.sendTransform((self.status_msg.position.x, self.status_msg.position.y, self.status_msg.position.z),
                        tf.transformations.quaternion_from_euler(0, 0, (self.status_msg.heading)/180*pi),
                        rospy.Time.now(),
                        "gps",
                        "map")
        self.is_status=True
                    
        # print(self.status_msg.yaw)    
if __name__ == '__main__':
    try:
        kcity_pathtracking=wecar_planner()
    except rospy.ROSInterruptException:
        pass
