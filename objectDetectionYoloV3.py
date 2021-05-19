#import neccessary python libraries
import numpy as np      
import cv2
import sys


def detectHumansFromVideo(weightFile,configFile,inputVideoFile,objectName):
# slow detection but very accurate accuracy
    net = cv2.dnn.readNet(weightFile,configFile)

    classes =[]
    with open(cocoFile,'r') as f:
        classes = f.read().splitlines()


    cap = cv2.VideoCapture(inputVideoFile)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    # Below VideoWriter object will create a frame of above defined sizeand the output is stored in output folder
    # with a name ipudtfilename_processed.MJPG
    outputFolder = '~/outputFiles'
    #outfilename to save the processed video to the disk
    outputFileName ='outputFiles/processedVideo.avi'
    resultFile = cv2.VideoWriter(outputFileName, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    while True :
        ret,frame = cap.read()
        if ret == True: 
            height, width,_ = frame.shape
            blob = cv2.dnn.blobFromImage(frame,1/255,(640,640),(0,0,0),swapRB= True,crop=False)
            net.setInput(blob)
            output_layer_names = net.getUnconnectedOutLayersNames()
            layerOutput = net.forward(output_layer_names)
            boxes =[]
            confidences=[]
            class_ids=[]
            for output in layerOutput:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence >0.5:
                        center_x =int(detection[0]* width)
                        center_y =int(detection[1]* height)
                        w  =int(detection[2]* width)
                        h  =int(detection[3]*height)
                        x= int (center_x - w/2)
                        y= int (center_y - h/2)
                        #to draw a rectangle around a frame
                        boxes.append([x,y,w,h])
                        #to display the confidence score
                        confidences.append((float(confidence)))
                        #to append the class name
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
            if len(indexes)!=0:
                font = cv2.FONT_HERSHEY_PLAIN
                colors = np.random.uniform(0,255,size=(len(boxes),3))
                for i in indexes.flatten():
                    x,y,w,h = boxes[i]
                    label = str(classes[class_ids[i]])
                    confidence= str(round(confidences[i],2 ))
                    color = colors[i]
                    #it will not detect the objects other than the passed object name from the terminal
                    # if label equals to passed object name then, it will draw a rectangle and print confidence score
                    if label == objectName:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                        cv2.putText(frame,label+" " + confidence,(x,y+20),font,2,(255,255,255),2)
                    else:
                        pass

            resultFile.write(frame)
            cv2.imshow('Frame',frame)
            #press s on the keyboard to interrupt the process
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    resultFile.release()
    cv2.destroyAllWindows()

#call the main function and initialize variables with terminal inputs
#configuration files kept inside configFiles folder
cocoFile = 'configFiles/coco.names'
configFile = 'configFiles/yolov3.cfg'
weightFile  = 'configFiles/yolov3.weights'

#input video file to be passed from terminal
# inputVideoFile = 'inputFiles/TopDown_AerialVideo_1080.mp4'
inputVideoFile = sys.argv[1]

#The object name that we want to detect will be passed from terminal
# objectNameForDetection = 'person'
objectNameForDetection = sys.argv[2]

#call the function to perform detection
detectHumansFromVideo(weightFile,configFile,inputVideoFile,objectNameForDetection)




