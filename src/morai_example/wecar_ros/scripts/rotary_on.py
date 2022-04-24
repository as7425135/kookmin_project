#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64, Int16
from sensor_msgs.msg import LaserScan

def laser_CB(msg):
    global lidar
    lidar = msg.ranges

def obstacle_x_CB(msg):
    global obstacle_x
    obstacle_x = msg.data

def obstacle_y_CB(msg):
    global obstacle_y
    obstacle_y = msg.data

def path_count_CB(msg):
    global path_count
    path_count = msg.data

def waypoint_CB(msg):
    global current_waypoint
    current_waypoint = msg.data

if __name__ == '__main__':
    try:
        lidar = []
        obstacle_x = 0.0
        obstacle_y = 0.0
        path_count = 0
        current_waypoint = 0
        go_stop = 1
        count = 0

        rospy.init_node('rotary_mission', anonymous=True)
        
        go_stop_pub = rospy.Publisher('/rotary_go_stop', Int16, queue_size=1)

        rospy.Subscriber('/lidar2D', LaserScan, laser_CB)
        rospy.Subscriber('/obstacle_x', Float64, obstacle_x_CB)
        rospy.Subscriber('/obstacle_y', Float64, obstacle_y_CB)
        rospy.Subscriber('/path_count', Int16, path_count_CB)
        rospy.Subscriber('/current_waypoint', Int16, waypoint_CB)
        
        rate = rospy.Rate(30)
        
        while not rospy.is_shutdown():
            front_ranges = []
            #1st rotary
            if path_count == 1 and 97 <= current_waypoint <= 102:
                print("웨이포인트 안")
                #print(obstacle_x)
                for i in range(215, 270):
	                if count == 0 and lidar[i] > 4.5:
	                    print("!!!!!!!!!!!")
	                    count = 1
	                else:
	                    count = 0
            elif path_count == 1 and 172 <= current_waypoint <= 180:
                count = 0
            #
            if path_count == 2 and 120 <= current_waypoint <= 127:
                print("웨이포인트 안")
                print(obstacle_x)
                if count == 0 and 10 <= obstacle_x <= 15 and obstacle_y <= -0.2: # 처음 진입할 때 장애물이 우측에 존재하면 count를 1로
                    print("!!!!!!!!!!!")
                    count = 1
                elif count == 1 and 10 > obstacle_x or obstacle_x > 15 or obstacle_y > -0.2:
                    count = 0
            
            if count == 1:
                if len(lidar) != 0:
                    for i in range(165, 206): # 좌 25도 우 15도 라이다 데이터 이용
                        if lidar[i] <= 1.0:
                            front_ranges.append(lidar[i])
                        if len(front_ranges) != 0 and min(front_ranges) < 0.8: 
                            go_stop = 0
                        else:
                            go_stop = 1
                if len(front_ranges) != 0:
                    print(front_ranges.index(min(front_ranges)))
                    print(min(front_ranges))
            elif count == 0:
                go_stop = 0
            go_stop_pub.publish(go_stop)
            print("count: %d" %count)
            print("go_stop: %d" %go_stop)
            
            rate.sleep()
    except rospy.ROSInterruptException:
        pass



    """
    x = 11.429, y = 0.048
    x = 14.138, y = -1.456
    y = 0 ~ -1.70 사이일 때 정지
    """