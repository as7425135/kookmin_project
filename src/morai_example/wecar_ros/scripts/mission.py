#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int16, Float64, Float64MultiArray,Float32
import time
from morai_msgs.msg import GetTrafficLightStatus

def path_count_CB(msg):
    global path_count
    path_count = msg.data

def waypoint_CB(msg):
    global current_waypoint
    current_waypoint = msg.data

def rotary_CB(msg):
    global rotary_sign
    rotary_sign = msg.data

def traffic_CB(msg):
    global traffic_sign
    traffic_sign = msg.trafficLightStatus

def dynamic_CB(msg) :
    global dynamic_array
    dynamic_array = msg.data

def person_CB(msg):
    global isPerson
    isPerson=msg.data

def personBbox_CB(msg):
    global personBbox
    personBbox=msg.data

def personDir_CB(msg):
    global person_dir
    person_dir=msg.data

if __name__ == '__main__':
    try:
        path_count = 0
        current_waypoint = 0
        rotary_sign = 0
        traffic_sign = 0
        dynamic_array = [0, 0]
        global time_count
        time_count = 1
        global timer
        global switch
        switch = 0
        timer = 0
        isPerson=-1
        person_dir=-1

        rospy.init_node('waypoin_control', anonymous=True)
        
        motor_pub = rospy.Publisher('/target_speed', Float64, queue_size=1)
        rospy.Subscriber('/path_count', Int16, path_count_CB)
        rospy.Subscriber('/current_waypoint', Int16, waypoint_CB)
        rospy.Subscriber('/rotary_go_stop', Int16, rotary_CB)
        rospy.Subscriber('/dynamic_Obstacle',Float64MultiArray, dynamic_CB)
        #rospy.Subscriber('/pub_trafficLight', Int16, traffic_CB)
        rospy.Subscriber('/GetTrafficLightStatus', GetTrafficLightStatus, traffic_CB)
        rospy.Subscriber("/pub_Isperson",Int16,)
        rospy.Subscriber('/pub_personbbox',Float32,personBbox_CB)
        rospy.Subscriber('/pub_personDir',Int16,personDir_CB)
        rate = rospy.Rate(30)
        
        while not rospy.is_shutdown():

            if path_count == 1 and 100 <= current_waypoint <= 163: # first rotary
                if rotary_sign == 0:
                    speed = 0
                elif rotary_sign == 1:
                    speed = 1
            
            elif path_count == 2 and 133 <= current_waypoint <= 196: # 
                if rotary_sign == 0:
                    speed = 0
                elif rotary_sign == 1:
                    speed = 1
        
            elif path_count == 1 and 248 <= current_waypoint <= 251: #
                print(traffic_sign)
                if traffic_sign == 33:
                    speed = 1
                    #print("!!!!!!!!!!!!!!!!!!!!!!!1")
                else:
                    speed = 0
            elif path_count == 2 and 76 <= current_waypoint <= 78: #
                print(traffic_sign)
                if traffic_sign == 33:
                    speed = 1
                else:
                    speed = 0


            elif path_count == 2 and 355 <= current_waypoint <= 516: #
                if(dynamic_array[0] == 1):
                    speed = 0.5
                if(dynamic_array[1] == 1 and time_count==1):
                    speed = 0
                    if(dynamic_array[1] == 0): 
                        speed = 1
                        time_count = 0
                    # elif( dynamic_array[1] == 1):
                    #     speed = 0
                # else:
                #      speed = 1

                if(dynamic_array[0] == 0 and dynamic_array[1] == 0):
                    time_count = 1
                    speed = 1





            elif path_count == 3 and 70 <= current_waypoint <=180: #
                if(dynamic_array[0] == 1):
                    speed = 0.5
                if(dynamic_array[1] == 1 and time_count==1):
                    speed = 0
                    if(dynamic_array[1] == 0): 
                        speed = 1
                        time_count = 0
                    # elif( dynamic_array[1] == 1):
                    #     speed = 0
                # else:
                #      speed = 1

                if(dynamic_array[0] == 0 and dynamic_array[1] == 0):
                    time_count = 1
                    speed = 1

            else:
                speed = 1
            """if path_count == 1 and current_waypoint >= 451: # 
                speed = 0"""


            motor_pub.publish(speed) # 
            # print("path_count: %d" %path_count)
            print("current_waypoint: %d" %current_waypoint)
            # print("rotary_sign: %d" %rotary_sign)
            print("target_speed: %d" %speed)
            #print("dynamic_speed: %d" %speed)
            
            #print(time_count)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass