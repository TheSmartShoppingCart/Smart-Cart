###### Main File -- Webcam

##### Webcam Object Detection Using TensorFlow-trained Classifer #####
##### Reference Link: https://www.youtube.com/watch?v=aimSGOAUI8Y&pp=ygU_aG93IHRvIHJ1biB0ZW5zb3JmbG93IGxpdGUgb24gcmFzcGJlcnJ5IHBpIGZvciBvYmplY3QgZGV0ZWN0aW9u
##### Reference Github: https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/deploy_guides/Raspberry_Pi_Guide.md

# Senior Design EECS 159A/B Fall 2023 UC Irvine

# This program uses TensorFlow Lite model to perform object detection on a live webcam
# It draws boxes and scores around around the objects of interest in each frame from the webcam
# It counts an item putting in/ taking out when moving across the line threshold
# To improve the FPS, the webcam object runs in a separate thread from the main program
# This script will work with regular USB webcam (not sure about PiCamera)

# Method of draw boxes, labels, and lines implemented using OpenCV


# Import Packages
import cv2
import numpy as np
import sys
import time


# external written files
import videostream
import interpreter
import framerate
import drawboundingbox 

# Global Constant
global inputMean = 127.5
global inputStd = 127.5

def webcam():
    # Set up Interpreter 
    interpret = interpreter.setupInterpreter()
    
    interPreter = interpret[0] 
    imW = interpret[1]
    imH = interpret[2]
    min_conf_threshold = interpret[3]
    labels = interpret[4] 
    
    interPreter.allocate_tensors()
    
    # Get model details
    inputDetails = interPreter.get_input_details()
    outputDetails = interPreter.get_output_details()
    height = inputDetails[0]['shape'][1]
    width = inputDetails[0]['shape'][2]
     
    floatingModel = (inputDetails[0]['dtype'] == np.float32)
    
    # Check output layer name to determine if this model was created with TF2 or TF1
    # output order is different for TF1 and TF2
    outname = outputDetails[0]['name']
    
    if('StatefulPartitionedCall' in outname): # TF2 model
        boxes_idx, classes_idx, scores_idx = 1,3,0
    else: # TF1 model
        boxes_idx, classes_idx, scores_idx = 0,1,2
    

    # Initialize frame rate calculation
    frameRateCal = 1
    frequency = framerate.init_FrameRate()
    
    # Initialize video stream
    videoStream = VideoStream(resolution=(imH, imW), framerate=30).start()
    time.sleep(1) # delay for 1 sec
    
    while (True):
        
        # Start timer (Calculate frame rate)
        t1 = cv2.getTickCount()
        
        # Grab frame from video stream
        frame1 = videoStream.read()
        
        # Acquire frame and resize to expected shape [1xHxWx3]
        frame = frame1.copy() # copy and put into the new frame
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameResized = cv2.resize(frameRGB, (width, height))
        inputData = np.expand_dims(frameResized, axis=0)
        
        # Normalize pixel values if using a floating model (ex: if model is non-quantized)
        if floatingModel :
            inputData = (np.float32(inputData) - inputMean) / inputStd
        
        # Perform the actual detection by running the model with the image as input
        interPreter.set_tensor(inputDetails[0]['index'],inputData)
        interPreter.invoke()
        
        # Retrieve detection result
        boxes = interPreter.get_tensor(outputDetails[boxes_idx]['index'])[0] # Bounding box coordinates of detected objects
        classes = interPreter.get_tensor(outputDetails[classes_idx]['index'])[0] # Class index of detected objects
        scores = interPreter.get_tensor(outputDetails[scores_idx]['index'])[0] # Confidence of detected objects
        
        # Loop over all detections and draw detection box if confidence is above minimum threshold
        for i in range(len(scores)):
            if((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
                
                # Get bounding box coordinates and draw box
                drawboundingbox.drawBoxAndLabel(frame, labels, imW, imH, boxes, classes, scores)
        
        # Draw framerate in the corner of frame
        cv2.putText(frame, 'FPS: {0: .2f)'.format(frameRateCal), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2, cv2.LINE_AA) 
        
        # Show the webcam
        cv2.imshow('WebCam', frame) 
        
        # Calculate the framerate
        t2 = cv2.getTickCount()
        frameRateCal = framerate.calculateFrameRate(t1, t2, frequency)
        
        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break 

    # Clean up
    cv2.destroyAllWindows()
    videoStream.stop() 
        
    
    
    


