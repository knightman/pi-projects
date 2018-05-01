# FunTest1.py

from sense_hat import SenseHat

# Fn to get the relative humidity from sense_hat
def report_humidity():
    h = SenseHat().get_humidity()
    return h

# Fn to get the temperature
def report_temperature():
    t = SenseHat().get_temperature()
    return t
