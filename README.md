# ML_Test_NewSpaceResearch
An object detection method using openCV YOLOV3 from a video.

# Problem Statement
Please run a computer vision and/or machine learning (CNN/DNN) based detector on this video, which should be able to detect humans present, draw a red bounding box
around them, and mention the probability of detection. Save the output video to disk.

# Dependencies
1. python 3.7.10
2. numpy  1.16.13
3. openCV 4.1.0

# How to install dependencies?
1. python (https://docs.python-guide.org/starting/install3/linux/)
2. numpy  (https://numpy.org/install/)
3. openCV (https://pypi.org/project/opencv-python/)

# How to Run?
$ python3 objectDetectionYoloV3.py 'path/input_video_file' 'Object name to be detected'
Examples:
1.  python3 objectDetectionYoloV3.py 'inputFiles/TopDown_AerialVideo_1080.mp4' 'person'
2.   python3 objectDetectionYoloV3.py 'inputFiles/TopDown_AerialVideo_1080.mp4' 'car'

