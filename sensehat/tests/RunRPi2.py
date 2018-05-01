# RunRPi2.py
#
# Created: Jan 19, 2016 by Andrew Knight
#
# Top-level run process on RPi2

import time
from sense_hat import SenseHat
from FunTest1 import report_humidity
from FunTest1 import report_temperature

sense = SenseHat()
sense.clear()

# color definitions for LEDs
white = (255, 255, 255)
none = (0, 0, 0)


def set_humidity_and_temperature():
    humidity = int(report_humidity())   #convert int for humidity %
    temperature = (report_temperature() * 1.8) + 32  #using float for temperature - convert to F

    # Determine H color based on humidity reading
    if humidity <= 15:
        H = [255, 0, 0]  # Red
    elif 15 < humidity <= 20:
        H = [255, 165, 0]  # Orange
    elif 20 < humidity <= 30:
        H = [255, 255, 0]  # Yellow
    elif 30 < humidity <= 45:
        H = [0, 255, 0]  # Green - ideal humidity range
    else:
        H = [255, 255, 255]  # White - value out of range

    # # Determine T color based on temperature reading
    # if temperature <= 20:  # 20degC is 68degF
    #     T = [128, 0, 128]  # Purple
    # elif 20 < temperature <= 21.2:  #21.2degC is about 70degF
    #     T = [0, 0, 255]  # Blue
    # elif 21.2 < temperature <= 22.8: #22.8degC is about 73degF
    #     T = [0, 255, 0]  # Green - ideal temp range
    # elif 22.8 < temperature <= 24:  #24degC is about 75.2degF
    #     T = [255, 255, 0]  # Yellow - getting warm
    # elif 24 < temperature <= 27:  #27degC is about 80degF
    #     T = [255, 165, 0]  # Orange - getting hot!
    # else:
    #     T = [255, 255, 255]  # White - value out of range

    # Determine T color based on temperature reading
    if temperature <= 65:  # 20degC is 68degF
        T = [128, 0, 128]  # Purple
    elif 65 < temperature <= 68:  #21.2degC is about 70degF
        T = [0, 0, 255]  # Blue
    elif 68 < temperature <= 72: #22.8degC is about 73degF
        T = [0, 255, 0]  # Green - ideal temp range
    elif 72 < temperature <= 74:  #24degC is about 75.2degF
        T = [255, 255, 0]  # Yellow - getting warm
    elif 74 < temperature <= 78:  #27degC is about 80degF
        T = [255, 165, 0]  # Orange - getting hot!
    elif 78 < temperature <= 85:  #27degC is about 80degF
        T = [255, 0, 0]  # Red - too hot!
    else:
        T = [255, 255, 255]  # White - value out of range

    # Draw the LED matrix with H and T
    O = [0, 0, 0]
    humidity_temperature = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        H, O, H, O, T, T, T, O,
        H, O, H, O, O, T, O, O,
        H, H, H, O, O, T, O, O,
        H, O, H, O, O, T, O, O,
        H, O, H, O, O, T, O, O
    ]

    # Set LED matrix
    sense.set_pixels(humidity_temperature)

    return  # end of Fn


# Run continuous check and update LED matrix
while True:
    # Scroll humidity %
    # sense.show_message(r"H% " + humidity)
    # sense.show_message(r"T " + temperature)

    # Heartbeat of top left LED to indicate running
    sense.set_pixel(0, 0, white)  # heatbeat ON - white LED at 0, 0
    time.sleep(1)
    # sense.set_pixel(0, 0, none) # heatbeat OFF - LED OFF at 0, 0
    set_humidity_and_temperature()
    time.sleep(1)
