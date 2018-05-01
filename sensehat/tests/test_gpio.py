# test_gpio.py
# Simple GPIO test on RPi

import RPi.GPIO as GPIO
pin = 18    # changed from pin 12, then 16

import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        print "LED on"
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(3)
        print "LED off"
        GPIO.output(pin, GPIO.LOW)
        time.sleep(3)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO