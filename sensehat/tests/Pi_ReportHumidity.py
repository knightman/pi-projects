# Pi_ReportHumidity.py
#
# Created: Jan 10, 2016 by Andrew Knight
#
# Simple script to read humidity on RPi

import time
from sense_hat import SenseHat

sense = SenseHat()
#humidity = sense.get_humidity()
#print("Humidity: %s %%rH" % humidity)

# alternatives
#print(sense.humidity)

# continue to print humidity reading every 5 seconds until break
var = 0
while var == 0 :
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    time.sleep(5)

print("exit")
