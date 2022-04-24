#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import LaserScan

class rotary_new():
    def __init__(self):

        go_stop = 1
        self.current_waypoint = 0
        self.path_count = 0
        count = 0
        self.rotary_array = [0,0,0]
        rospy.init_node('rotary', anonymous=True)

        go_stop_pub = rospy.Publisher('/rotary_go_stop', Int16, queue_size=1)

        rospy.Subscriber("/lidar2D", LaserScan, self.rotary_obstacle)
        rospy.Subscriber('/path_count', Int16, self.path_count_CB)
        rospy.Subscriber('/current_waypoint', Int16, self.waypoint_CB)

        rate = rospy.Rate(30)

        while not rospy.is_shutdown():

            front_ranges = []  # 
            

            if self.path_count == 1 and 97 <= self.current_waypoint <= 102:      # 
                print("aaa")
                if(self.rotary_array[0]==1 and count == 0):
                    print("rotary : " , self.rotary_array)
                    go_stop = 0
                    if(self.rotary_array[1] == 1 or self.rotary_array[2] == 1):
                        go_stop = 0
                    else:
                        go_stop = 1
                        count = 1              # 
        
            if self.path_count == 2 and 107<= self.current_waypoint <= 110: 
                count = 0
                
            if self.path_count == 2 and 130 <= self.current_waypoint <= 135:     # 
                print("bbb")

                if(count == 0 and self.rotary_array[0]==1):
                    go_stop = 0
                    if(self.rotary_array[1] == 1 or self.rotary_array[2] == 1):
                        go_stop = 0
                    else:
                        go_stop = 1
                        count = 1              #
            
               
    
            if count == 1:
                if len(self.lidar_origin) != 0:
                    for i in range(165, 206): #
                        if self.lidar_origin[i] <= 1.0:
                            front_ranges.append(self.lidar_origin[i])
                        if len(front_ranges) != 0 and min(front_ranges) < 0.8: 
                            go_stop = 0
                        else:
                            go_stop = 1
                if len(front_ranges) != 0:
                    print(front_ranges.index(min(front_ranges)))
                    print(min(front_ranges))
            # elif count == 0:
            #     go_stop = 1           

            go_stop_pub.publish(go_stop)
            print("count: ", count)
            print("go_stop: ", go_stop)
            rate.sleep()

    # def laser_callback(self, msg):
        
    #     #print(lidar_origin)

    def path_count_CB(self, msg):
        self.path_count = msg.data

    def waypoint_CB(self, msg):
        self.current_waypoint = msg.data

    def rotary_obstacle(self, msg):
        self.lidar_origin = list(msg.ranges)
        self.rotary_array = [0, 0, 0]
        count  = 0

        for r in self.lidar_origin:
            if(90 <= count <= 270 and r < 5):   # 
                self.rotary_array[0] = 1      # 

            if(180 <= count <= 270 and r < 2.1):  #
                self.rotary_array[1] = 1 

            if(90 <= count <= 180 and r < 1.2): #
                self.rotary_array[2] = 1 

            
            count += 1 


        



if __name__ == '__main__':
    
    try:
        rotary = rotary_new()
    except rospy.ROSInterruptException:
        pass

            