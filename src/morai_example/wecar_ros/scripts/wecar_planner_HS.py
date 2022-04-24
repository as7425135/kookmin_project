#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os
import rospy
import rospkg
import numpy as np
from nav_msgs.msg import Path,Odometry
from std_msgs.msg import Float64,Int16,Float32MultiArray
from geometry_msgs.msg import PoseStamped,Point
from morai_msgs.msg import EgoVehicleStatus,CtrlCmd,GetTrafficLightStatus,SetTrafficLight #변경 (ObjectStatusList 삭제)
from lib.utils import pathReader, findLocalPath,purePursuit,pidController,velocityPlanning,latticePlanner#변경 cruiseControl,vaildObject 삭제
import tf
from math import cos,sin,sqrt,pow,atan2,pi
import time


class wecar_planner():
    def __init__(self):
        rospy.init_node('wecar_planner', anonymous=True)

        arg = rospy.myargv(argv=sys.argv)
        self.path_name_1=arg[1]
        self.path_name_2=arg[2]
        self.path_name_3=arg[3]
        self.path_name_4=arg[4]
        path_count = 1
        global timer
        timer = 0
        time_count = 1
        goal = False # 1 초기값, 2은 도착, 3는 목표 도착 안함
        

        #publisher
        global_path_pub= rospy.Publisher('/global_path',Path, queue_size=1) ## global_path publisher
        local_path_pub= rospy.Publisher('/local_path',Path, queue_size=1) ## local_path publisher
        self.motor_pub = rospy.Publisher('commands/motor/speed',Float64, queue_size=1)
        self.servo_pub = rospy.Publisher('commands/servo/position',Float64, queue_size=1)
        ########################  lattice  ########################
        for i in range(1,8):            
            globals()['lattice_path_{}_pub'.format(i)]=rospy.Publisher('lattice_path_{}'.format(i),Path,queue_size=1)  
        ########################  lattice  ########################
        
        #subscriber
        rospy.Subscriber("/Ego_topic", EgoVehicleStatus, self.statusCB) ## Vehicl Status Subscriber 
        #rospy.Subscriber("/Object_topic", ObjectStatusList, self.objectInfoCB) ## Object information Subscriber

        #def
        self.is_status=False ## 차량 상태 점검
        #self.is_obj=True ## 장애물 상태 점검. (변경)
        self.steering_angle_to_servo_offset=0.5304 ## servo moter offset
        self.rpm_gain = 4616
        self.motor_msg=Float64()
        self.servo_msg=Float64()
        

        #class
        path_reader=pathReader('wecar_ros') ## 경로 파일의 위치
        pure_pursuit=purePursuit() ## purePursuit import
        #self.cc=cruiseControl(0.5,1) ## cruiseControl import (object_vel_gain, object_dis_gain)
        #self.vo=vaildObject() ## 장애물 유무 확인 ()  #변경
        pid=pidController() ## pidController import
        

        #read path
        self.global_path=path_reader.read_txt(self.path_name_1+".txt") ## 출력할 경로의 이름
        self.global_path_1=path_reader.read_txt(self.path_name_4+".txt") ## 출력할 경로의 이름
        vel_planner=velocityPlanning(1,0.15) ## 속도 계획
        vel_profile=vel_planner.curveBasedVelocity(self.global_path_1,30)
        

        
        #time var
        count=0
        rate = rospy.Rate(30) # 30hz

        lattice_current_lane=3

        while not rospy.is_shutdown():
            print(self.is_status)
                        
            if self.is_status==True : #and self.is_obj==True: ## 차량의 상태, 장애물 상태 점검
                ## global_path와 차량의 status_msg를 이용해 현제 waypoint와 local_path를 생성
                local_path,self.current_waypoint=findLocalPath(self.global_path,self.status_msg) 
                
                ## 장애물의 숫자와 Type 위치 속도 (object_num, object type, object pose_x, object pose_y, object velocity)
                #self.vo.get_object(self.object_num,self.object_info[0],self.object_info[1],self.object_info[2],self.object_info[3])
                #global_obj,local_obj=self.vo.calc_vaild_obj([self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi]) #변경

                ########################  lattice  ########################
                vehicle_status=[self.status_msg.position.x,self.status_msg.position.y,(self.status_msg.heading)/180*pi,self.status_msg.velocity.x/3.6]
                lattice_path,selected_lane=latticePlanner(local_path,vehicle_status,lattice_current_lane)#(local_path,global_obj,vehicle_status,lattice_current_lane) 변경
                lattice_current_lane=selected_lane
                                
                if selected_lane != -1: 
                    local_path=lattice_path[selected_lane]                
                
                if len(lattice_path)==7:                    
                    for i in range(1,8):
                        globals()['lattice_path_{}_pub'.format(i)].publish(lattice_path[i-1])
                ########################  lattice  ########################
            
                #self.cc.checkObject(local_path,global_obj,local_obj) #변경 cruise controll

                
                pure_pursuit.getPath(local_path) ## pure_pursuit 알고리즘에 Local path 적용
                pure_pursuit.getEgoStatus(self.status_msg) ## pure_pursuit 알고리즘에 차량의 status 적용

                self.steering=pure_pursuit.steering_angle()
                
                #self.cc_vel = self.cc.acc(local_obj,self.status_msg.velocity.x,vel_profile[self.current_waypoint],self.status_msg) ## advanced cruise control 적용한 속도 계획  변경

                self.servo_msg = self.steering*0.021 + self.steering_angle_to_servo_offset
                #self.motor_msg = self.cc_vel *self.rpm_gain /3.6 #변경
                self.motor_msg = vel_profile[self.current_waypoint]*self.rpm_gain /3.6 #변경
                                
                
    
                local_path_pub.publish(local_path) ## Local Path 출력

                self.servo_pub.publish(self.servo_msg)
                #self.motor_pub.publish(self.motor_msg)
                self.print_info()
            
            if count==300 : ## global path 출력
                global_path_pub.publish(self.global_path)
                count=0
            count+=1
            
            if path_count == 1 and 45 <= self.current_waypoint <= 47: # 정지선 앞 웨이포인트 확인 해야함, path_name_1일 때 정지선 도착하면 goal이 True로 바뀜
                goal = True
            elif path_count == 1: #and self.current_waypoint != 46:
                goal = False

            if goal == True and time_count == 1: # goal == True이면 타이머 시작
                init_time = time.time()
                time_count = 2
            elif goal == True and time_count == 2:
                timer = time.time() - init_time
            
            
            if goal == True and timer <= 5: # 목표 도착하면 5초동안 정지
                self.motor_pub.publish(0)
            else:
                self.motor_pub.publish(self.motor_msg)

            if path_count == 1 and self.current_waypoint == 327:
                self.global_path=path_reader.read_txt(self.path_name_2+".txt")
                path_count = 2

            if path_count == 2 and self.current_waypoint == 725:
                self.global_path=path_reader.read_txt(self.path_name_3+".txt")
            rospy.loginfo(timer)
            rate.sleep()


    def print_info(self):

        os.system('clear')
        print('--------------------status-------------------------')
        print('position :{0} ,{1}, {2}'.format(self.status_msg.position.x,self.status_msg.position.y,self.status_msg.position.z))
        print('velocity :{} km/h'.format(self.status_msg.velocity.x))
        print('heading :{} deg'.format(self.status_msg.heading))

#        print('--------------------object-------------------------')
#        print('object num :{}'.format(self.object_num))
#        for i in range(0,self.object_num) :
#            print('{0} : type = {1}, x = {2}, y = {3}, z = {4} '.format(i,self.object_info[0],self.object_info[1],self.object_info[2],self.object_info[3]))

        print('--------------------controller-------------------------')
        #print('target vel_planning :{} km/h'.format(self.cc_vel))
        print('target steering_angle :{} deg'.format(self.steering))

        print('--------------------localization-------------------------')
        print('all waypoint size: {} '.format(len(self.global_path.poses)))
        print('current waypoint : {} '.format(self.current_waypoint))


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

#    def objectInfoCB(self,data): ## Object information Subscriber
#        self.object_num=data.num_of_npcs+data.num_of_obstacle+data.num_of_pedestrian
#        object_type=[]
#        object_pose_x=[]
#        object_pose_y=[]
#        object_velocity=[]
#        for num in range(data.num_of_npcs) :
#            object_type.append(data.npc_list[num].type)
#            object_pose_x.append(data.npc_list[num].position.x)
#            object_pose_y.append(data.npc_list[num].position.y)
#            object_velocity.append(data.npc_list[num].velocity.x)
#
#        for num in range(data.num_of_obstacle) :
#            object_type.append(data.obstacle_list[num].type)
#            object_pose_x.append(data.obstacle_list[num].position.x)
#            object_pose_y.append(data.obstacle_list[num].position.y)
#            object_velocity.append(data.obstacle_list[num].velocity.x)
#
#        for num in range(data.num_of_pedestrian) :
#            object_type.append(data.pedestrian_list[num].type)
#            object_pose_x.append(data.pedestrian_list[num].position.x)
#            object_pose_y.append(data.pedestrian_list[num].position.y)
#            object_velocity.append(data.pedestrian_list[num].velocity.x)
#
#        self.object_info=[object_type,object_pose_x,object_pose_y,object_velocity]
#        self.is_obj=True
    
if __name__ == '__main__':
    try:
        kcity_pathtracking=wecar_planner()
    except rospy.ROSInterruptException:
        pass
