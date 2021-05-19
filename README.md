# ML_Test_NewSpaceResearch
An object detection method using openCV YOLOV3 from a video.

# Problem Statement
Please run a computer vision and/or machine learning (CNN/DNN) based detector on this video, which should be able to detect humans present, draw a red bounding box
around them, and mention the probability of detection. Save the output video to disk.

# YOLOV3
**You Only Look Once** or more popularly known as YOLO is one of the fastest real-time object detection algorithm (45 frames per seconds) as compared to R-CNN family (R-CNN, Fast R-CNN, Faster R-CNN, etc.)
Instead of selecting some regions, YOLO applies a neural network to the entire image to predict bounding boxes and their probabilities.
We load the YoloV3 weights and configuration file with the help of dnn module of OpenCV. coco.names file contains the names of the different objects that our model has been trained to identify. We deteect the object and draw a rectangle and print the confidence score along with the class name.


# Dependencies
1. python 3.7.10
2. numpy  1.16.13
3. openCV 4.1.0
4. YoloV3 wights and config files
5. CoCOnames file
# How to install dependencies?
1. python (https://docs.python-guide.org/starting/install3/linux/)
2. numpy  (https://numpy.org/install/)
3. openCV (https://pypi.org/project/opencv-python/)
4. Save coconames file inside the folder 'configFiles/' from the link (https://github.com/pjreddie/darknet/blob/master/data/coco.names)
5. Save weights and config yolov3 files from the link (https://pjreddie.com/darknet/yolo/)
  a. config file (https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
  b. weight files(https://pjreddie.com/media/files/yolov3.weights)



# How to Run?

Due to size constraint of 25MB the weights file is not copied to the folder 'configFiles/', therefore before running the below command download the weights file from the location (https://pjreddie.com/media/files/yolov3.weights) and place it inside the folder 'configFile' (or) you can download the whole scripts anf file from the following gdrive:
https://drive.google.com/drive/folders/1LDPuxdMGsV_9JQhlptvE95iG09qu-rth?usp=sharing


$ python3 objectDetectionYoloV3.py 'path/input_video_file' 'Object name to be detected'
Examples:
1.  python3 objectDetectionYoloV3.py 'inputFiles/TopDown_AerialVideo_1080.mp4' 'person'
2.   python3 objectDetectionYoloV3.py 'inputFiles/TopDown_AerialVideo_1080.mp4' 'car'

*Note:-*
1. You can press 'q' key from your keyboard to interrupt the current process anytime.
2. The processed video will be saved in the 'outputFiles/' folder.
