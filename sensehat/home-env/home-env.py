import time, datetime
from sense_hat import SenseHat
sh = SenseHat()

while(True):
    #reading = {'timestamp': str(datetime.datetime.now()), 'temp': str(sh.get_humidity()), 'hum': str(sh.get_temperature())}
    timest = str(datetime.datetime.now())
    temp = str(round(sh.get_humidity(), 1))
    hum = str(round(sh.get_temperature(), 1))
    
    with open('logfile.txt', 'a+') as f:
        #f.write(str(reading) + '\n')
        f.write(timest + ', ' + temp + ', ' + hum + '\n')
    
    time.sleep(60)