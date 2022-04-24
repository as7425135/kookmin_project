#! /usr/bin/env python3

import rospy
import math
from morai_msgs.msg import EgoVehicleStatus
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

def laser_callback(msg):
    global lidar
    lidar = list(msg.ranges)

def Ego_callback(msg):
    global ego_x
    global ego_y
    global heading
    ego_x = msg.position.x
    ego_y = msg.position.y
    heading = msg.heading
    if heading > 180:
        heading - 360 # 0 ~ 180도, 0 ~ -180도로 바꾸기 위함

if __name__ == '__main__':
    try:
        lidar = []
        lidar_angle = []
        ego_x = 0.0
        ego_y = 0.0
        heading = 0.0
        d = 0.115 # 차량 중심과 라이다 사이의 거리
        DtoR = math.pi / 180

        rospy.init_node('coordinate', anonymous=True)
        obstacle_x_pub = rospy.Publisher('/obstacle_x', Float64, queue_size=1)
        obstacle_y_pub = rospy.Publisher('/obstacle_y', Float64, queue_size=1)
        rospy.Subscriber('/lidar2D', LaserScan, laser_callback)
        rospy.Subscriber('/Ego_topic', EgoVehicleStatus, Ego_callback)
        rate = rospy.Rate(30)

        while not rospy.is_shutdown():
            obstacle_x = []
            obstacle_y = []
            obstacle_position = []
            lidar_x = ego_x + d*math.cos(heading)
            lidar_y = ego_y + d*math.sin(heading)
            
            for i in range(0, len(lidar)):
                '''
                ia = i -1
                ib = i + 1
                if ia == -1:
                    ia = 1
                if ib == 360:
                    ib = 358'''
                if lidar[i] < 1.5: #and lidar[ia] < 5 or lidar[i] and lidar[ib] < 5:
                    r = lidar[i]
                    lidar_angle = i + 180
                    if lidar_angle > 360:
                        lidar_angle = lidar_angle - 360
                    #lidar_angle = lidar_angle + 180 # 라이다가 180도 돌아가 있어서
                    a = lidar_x + r*math.cos(DtoR*(heading + lidar_angle))
                    b = lidar_y + r*math.sin(DtoR*(heading + lidar_angle))
                    obstacle_x.append(a)
                    obstacle_y.append(b)
            for j in range(0, len(obstacle_x)):
                obstacle_position.append([obstacle_x[j], obstacle_y[j]])
            
            if len(obstacle_x) != 0 and len(obstacle_y) != 0:
                print("X")
                print(obstacle_x)
                print("Y")
                print(obstacle_y)
                #print(min(lidar))
                #print(lidar_angle)
                obstacle_x_pub.publish(obstacle_x[0])
                obstacle_y_pub.publish(obstacle_y[0])
            rate.sleep()
    except rospy.ROSInterruptException:
        pass