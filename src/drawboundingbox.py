# Display Bounding Box and Label

import cv2

def drawBoxAndLabel(frame, labels, imW, imH, boxes, classes, scores, i):
    # Get bounding box coordinates and draw box
    # Interpreter can return coordinates that are outside of image dimensions, need to force them
    # to be within image using using max() and min()
    ymin = int(max(1, (boxes[i][0] * imH))) # topLeft y-axis
    xmin = int(max(1, (boxes[i][1] * imW))) # topLeft x-axis
    ymax = int(min(imH, (boxes[i][2] * imH))) # bottomRight y-axis
    xmax = int(min(imW, (boxes[i][3] * imW))) # bottomLeft x-axis
    
    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10,255,0), 2) 
    
    # Draw Label
    objectName = labels[int(classes[i])] # Look up object name from "labels" array using class index
    label = '%s: %d%%' % (objectName, int(scores[i]*100)) # Example: 'person: 72%'
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
    label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of the window
    # Draw white box to put label text in 
    cv2.rectangle(frame, (xmin, label_ymin - labelSize[1] - 10), (xmin + labelSize[0], label_ymin + baseLine - 10), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2) # Draw label text
    
    