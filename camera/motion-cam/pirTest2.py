import time
from datetime import datetime
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Module Test started")
    start_time = time.time()
    time.sleep(1)
    count = 0
    camera = PiCamera()

    while True:
        inputTrigger = GPIO.input(PIR_PIN)
        if inputTrigger:
            count = count + 1               #increase total motion count
            print("Motion Detected!")       #print motion detection, later will want to log it
            filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
            camera.start_recording(filename)    #start recording
            time.sleep(5)                       #record for five seconds
            camera.stop_recording()             #stop recording
        time.sleep(2)                   # delay in seconds
except KeyboardInterrupt:
    print("...Program Interrupt")
    print("Total Motion Count: " + str(count))
    print("Elapsed Time: " + str(time.time() - start_time))
    GPIO.cleanup()
