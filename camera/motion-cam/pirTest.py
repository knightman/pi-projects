import time
from datetime import datetime
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
RECORDING = False

def start_record():
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")    #create timestamped file
    camera.start_recording(filename)    #start recording
    #time.sleep(3)                       #record for three seconds minimum
    RECORDING = True                    # set recording flag
    return

def stop_record():
    camera.stop_recording()             #stop recording
    RECORDING = False
    return

try:
    print("PIR Module Test started")
    start_time = time.time()
    time.sleep(1)
    count = 0
    camera = PiCamera()

    while True:
        inputTrigger = GPIO.input(PIR_PIN)
        if (inputTrigger and not RECORDING):
            count = count + 1               #increase total motion count
            print("Motion Detected!")       #print motion detection, later will want to log it
            start_record()                  #record motion!
        time.sleep(2)                       # loop delay in seconds - smooth out sensor readings
        if (not inputTrigger and RECORDING):
            stop_record()
except KeyboardInterrupt:
    print("...Program Interrupt")
    print("Total Motion Count: " + str(count))
    print("Elapsed Time: " + str(time.time() - start_time))
    GPIO.cleanup()
