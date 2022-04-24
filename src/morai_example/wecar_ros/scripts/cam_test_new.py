#!/usr/bin/env python3

# from ctypes.wintypes import BOOLEAN
import cv2 as cv
# import time
import rospy

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge,CvBridgeError
# from vision_msgs.msg import Detection2D
# from vision_msgs.msg import Detection2DArray
# from vision_msgs.msg import BoundingBox2D
# from vision_msgs.msg import ObjectHypothesisWithPose
from std_msgs.msg import Float32MultiArray, Int16,Float32 # for sending msg class, confidence inform 


def callback(data):
    # simulation cam -> cv2
    global traffic_go_stop
    global per_center
    global is_person
    global count
    global tmp_center
    global per_dir
    try:
        frame = bridge.compressed_imgmsg_to_cv2(data) # ros image message를 cv_image data로 변환
    except CvBridgeError as e:
        print("converting error")
        print(e)

    classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)


    is_person=0
    traffic_go_stop=0
    per_center=-1


    for (classid, score, box,i) in zip(classes, scores, boxes,range(len(boxes))):
        if score>0.97:
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f"%(class_name[classid], score)
            # print(label)
            cv.rectangle(frame, box, color, 1)
            cv.putText(frame, label, (box[0], box[1]-10),
                cv.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
            


            center_x = boxes[0][0] + (boxes[0][2])/2 # get bounding center x
            # center_y = boxes[i][1] + (boxes[i][3])/2 # get bounding cetner y
            # print('after',center_x)

            if classid==0:
                is_person=1
                per_center=center_x
            
            if classid==5:
                traffic_go_stop=1
            elif classid==1 or classid==2:
                traffic_go_stop=0

    if per_center==-1:
        per_dir=-1
    elif per_center-tmp_center>5:
        per_dir = 0 # left -> right
        print('left -> right')
        print('bbox',per_center)
    elif per_center-tmp_center<-5:
        per_dir =1 # right -> left
        print('right -> left')
        print('bbox',per_center)

    if count %2 ==0:
        tmp_center=per_center
    

    # print('traffic',traffic_go_stop)
    # print('person',is_person)
    # print('bbox',per_center)
    count+=1
    # cv.imshow('frame', frame)
    # cv.waitKey(1)

if __name__=="__main__":

    rospy.init_node('image_to_receiver', anonymous=False)
    pubcam = rospy.Publisher("/pub_image", Image, queue_size=10)
    subcam = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, callback)
    pubtraffic=rospy.Publisher("/pub_trafficLight",Int16,queue_size=1)
    pubpersonbbox=rospy.Publisher("/pub_personbbox",Float32,queue_size=1)
    pubIsperson=rospy.Publisher("/pub_Isperson",Int16,queue_size=1)
    pubpersondir=rospy.Publisher("/pub_personDir",Int16,queue_size=1)

    bridge = CvBridge()
    traffic_go_stop=1
    per_center=0
    is_person=0
    count=0
    tmp_center=0
    per_dir=-1

    Conf_threshold = 0.4
    NMS_threshold = 0.4
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

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        try:
            pubtraffic.publish(traffic_go_stop)
            pubpersonbbox.publish(per_center)
            pubIsperson.publish(is_person)
            pubpersondir.publish(per_dir)
            rate.sleep()
        except CvBridgeError as e:
            print("publish error")
            print(e)