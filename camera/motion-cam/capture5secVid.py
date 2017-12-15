#capture5secVideo.py
import time
from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")    #create timestamped file
camera.start_recording(filename)    #start recording
time.sleep(5)                       #record for 5 seconds
camera.stop_recording()             #stop recording
