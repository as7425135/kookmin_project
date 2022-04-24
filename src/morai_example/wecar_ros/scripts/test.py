import time

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import rospy
from cv_bridge import CvBridge, CvBridgeError
from scipy.signal import butter, freqz, lfilter
from sensor_msgs.msg import CompressedImage, Image

Conf_threshold = 0.5
NMS_threshold = 0.5
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class_name = []
with open('custom.txt', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]
net = cv.dnn.readNet('wecar_yolov4_tiny.weights', 'wecar_yolo4_tiny.cfg')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


order = 6
fs = 30.0       
cutoff = 3.667  


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

b, a = butter_lowpass(cutoff, fs, order)



class camera_sim():
    def __init__(self):
        rospy.init_node('image_to_receiver', anonymous=False)
        self.pubcam = rospy.Publisher("/pub_image", Image, queue_size=10)
        self.subcam = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        self.bridge = CvBridge()
        rospy.on_shutdown(self.cam_shutdown)
        rospy.spin()

    def callback(self, data):
        # simulation cam -> cv2
        try:
            frame = self.bridge.compressed_imgmsg_to_cv2(data) # ros image message를 cv_image data로 변환

        except CvBridgeError as e:
            print("converting error")
            print(e)
        classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)

        for (classid, score, box,i) in zip(classes, scores, boxes,range(len(boxes))):
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f"%(class_name[classid], score)
            # print(box)
            # print(label)
            cv.rectangle(frame, box, color, 1)
            cv.putText(frame, label, (box[0], box[1]-10),
                cv.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
            center_x = boxes[i][0] + (boxes[i][2])/2 # get bounding center x
            center_y = boxes[i][1] + (boxes[i][3])/2 # get bounding cetner y
            print(center_x)
            if classid==0:
                per_center=center_x
                is_person=1
            
            if classid==5:
                traffic_go_stop=1
            elif classid==1 or classid==2:
                traffic_go_stop=0
        # tmp=0
        # tmp_arr=[]
        # tmp2=0
        # for i in range(len(boxes)):
        #     for _ in boxes:
        #         if scores[i]>=0.8 and classes[i]==4:
        #             # print(boxes)
                    

        #             center_x = boxes[i][0] + (boxes[i][2])/2 # get bounding center x
        #             center_y = boxes[i][1] + (boxes[i][3])/2 # get bounding cetner y
        #             if tmp2==0:
        #                 print('GO')
        #             # elif center_x>192 and center_x - tmp<=0:
        #             #     print('GO')
        #             else:
        #                 print('STOP')
        #                 print(center_x - tmp)
        #             size_y_str=str(boxes[i][3])+' '
        #             # print(tmp)

        #             # print("x,y:",center_x,center_y)
        #             # with open('data.txt', 'a') as f:
        #             #     f.write(size_y_str)
        #             # print('size y:',size_y_str)
        #             # print('size x:',boxes[i][2])
        #             # print(scores[i])
        #             # print(classes[i]) # append class inform to list

        #             tmp_arr.append(center_x-tmp)
        #             if len(tmp_arr)==10:
        #                 tmp2=tmp_arr.pop()

        #             tmp=center_x
        #             # print(tmp)

        cv.imshow('frame', frame)
        cv.waitKey(1)

    def cam_shutdown(self):
        print("I'm dead!")


cs=camera_sim()
