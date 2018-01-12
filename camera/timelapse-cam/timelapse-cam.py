# timelapse-cam.py
from picamera import PiCamera
import time, datetime

camera = PiCamera()

#filename = '/home/pi/v/video{}.h264'.format(datetime.datetime.now())
filename = '/home/pi/v/video1.h264'
camera.start_recording(filename)
time.sleep(3)
camera.stop_recording()