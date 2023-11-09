from ultralytics import YOLO
import cv2
import math
import pandas as pd
from tracker import *


# line coordinate
# L1_x_s = 4 # line 1, start x-coordinate
# L1_x_e = 620 # line1, end x-coordinate
# L1_y = 120  # line 1, y-coordinate
#
# L2_x_s = 20 # line 2, start x-coordinate
# L2_x_e = 624 # line 2, end x-coordinate
# L2_y = 200
# offset = 6
#
# YELLOW = (0, 255, 255)

'''
BOTTLE = 39,
CUP = 41,
BANANA = 46,
APPLE = 47,
ORANGE =  49,
BROCCOLI = 50,
CARROT = 51,
PIZZA = 53,
DONUT = 54,
CAKE = 55
'''
# itemList = ['bottle']
itemList = [39, 41, 46, 47, 49, 50, 51, 53, 54, 55]

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# Using Yolov8 nano
# model = YOLO('../YOLO_Weights/yolov8n.pt')
model = YOLO('yolov8n.pt')
# model.predict(source=0, show=True, stream=True, classes=0) # for class person
# for i in range(0,len(itemList)):
#     model.predict(source=0, show=True, stream=True, classes=itemList[i])


classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
# Goal: Detect mulitple items of the specific lists below

# classNames = ["apple", "banana", "orange", "broccoli",
#               "carrot", "donut", "pizza", "cake", "bottle", "cup"]



while True:
        success, img = cap.read()

        # Doing detections using Yolov8 frame by frame
        # stream = True will use the generator and it is more efficient than normal
        results = model(img, stream=True)

        # Once we have the results we can check for individual bounding boxes and see how well it performs
        # Once we have the results we will loop through them and we will have the bounding boxes for each of the result
        # we will loop through each of the bouncing box
        for r in results:
            boxes = r.boxes
            for box in boxes:

                conf = math.ceil((box.conf[0] * 100)) / 100
                # cls: class ID
                cls = int(box.cls[0])
                # print(cls)

                for i in range(0, len(itemList)):
                    if(cls == itemList[i]):
                # retrieve the name of the class from ID
                        class_name = classNames[cls]

                # # For Debugging
                # for i in range(0, len(itemList)):
                #     if (class_name == itemList[i]):

                        # (x1,y1) : top left corner of a box
                        # (x2, y2) : bottom right corner of a box
                        x1, y1, x2, y2 = box.xyxy[0]
                        #print(x1, y1, x2, y2)
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        print(x1, y1, x2, y2)
                        # print out the rectangle of the img with coordinate, color, thickness
                        cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255), 3)
                        #print(box.conf[0])
                        # box.conf : show confidence prediction value

                # conf = math.ceil((box.conf[0]*100)) / 100
                # # cls ID
                # cls = int(box.cls[0])
                # print(cls)
                # # retrieve the name of the class from ID
                # class_name = classNames[cls]

                    # label of each class with its confidence value
                        label = f'{class_name}:{conf}'
                    # Text size of the label
                        t_size = cv2.getTextSize(label, 0, fontScale=2, thickness=1)[0]
                        print(t_size)
                        c2 = x1 + t_size[0], y1 - t_size[1] - 3
                        cv2.rectangle(img, (x1,y1), c2, [255,0,255], -1, lineType=cv2.LINE_AA)
                        cv2.putText(img, label, (x1,y1-2), 0, 1, [255,255,255], thickness=1, lineType=cv2.LINE_AA)



        # # Line 1:      start point   end point   color      thickness
        # cv2.line(img, (L1_x_s, L1_y), (L1_x_e, L1_y), (255, 255, 255), 1)
        # # Put text: Line1
        # #                   String    (x,y)         Font                 Font Scale  Color    Thickness
        # cv2.putText(img, "Line 1", (6, 120), cv2.FONT_HERSHEY_COMPLEX, 0.8, YELLOW, 2)
        # # Line 2
        # cv2.line(img, (L2_x_s, L2_y), (L2_x_e, L2_y), (255, 255, 255), 1)
        # # Put text: Line2
        # cv2.putText(img, "Line 2", (26, 200), cv2.FONT_HERSHEY_COMPLEX, 0.8, YELLOW, 2)


        out.write(img)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF==ord('1'):
            break

out.release()