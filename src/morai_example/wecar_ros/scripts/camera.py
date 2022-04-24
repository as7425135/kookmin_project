#!/usr/bin/env python3
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage

class IMGParser:
    def __init__(self):
        global count
        rospy.init_node('camera', anonymous=True)
        count=0
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        rospy.spin()

    def callback(self, data):
        global count
        # rate = rospy.Rate(3)
        np_arr = np.fromstring(data.data, np.uint8)
        img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imshow("Image window", img_bgr)
        cv2.imwrite('./img/img%d.jpg'%count,img_bgr)
        count+=1
        cv2.waitKey(1)
        # rate.sleep()

if __name__ == '__main__':
    try:
        image_parser = IMGParser()
    except rospy.ROSInterruptException:
        pass
