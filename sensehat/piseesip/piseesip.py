# piseesip.py
# Displays the eth0 ipaddr as scrolling text on the pihat led matrix
#TODO: should probably config to run this upon startup...

from time import sleep
from sense_hat import SenseHat
from netifaces import AF_INET
import netifaces as ni

sense = SenseHat()
#ipaddr = ni.ifaddresses('eth0')[AF_INET][0]['addr']
ipaddr = ni.ifaddresses('wlan0')[AF_INET][0]['addr']

while(True):
	event = sense.stick.wait_for_event()
	print('joystick was {} {}'.format(event.action, event.direction))
	sense.show_message(ipaddr)
	sleep(1)

