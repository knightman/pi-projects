# piseesip

For displaying my ip address on a headless pi.

#### Description

I love using the Raspberry Pi to test many different applications, even when I'm on the go. However it is sometimes difficult to keep track of what it is currently being used for, or even how to connect.
After initial setup, I typically only need to ssh into the device to find which programs I currently have running but without finding a monitor and keyboard. When PiHat is installed, this handy little script will display the ip address regardless of the network I'm conneted to.

#### Instructions

But first, some assumptions... you must have Raspbian or other OS installed with ssh enabled and a known username/password.
PLEASE CHANGE THE PASSWORD FROM THE DEFAULT!
Also, you must have the SenseHat installed and modules loaded. For details about initial device setup, please refer to raspberrypi.org.
Finally, you do the basic setup on your device including wlan configuration to connect to your network and installing updates.

The piseesip.py file can be used basically unchanged to display the current IP address. For this to be useful in headless mode, we need to configure the pi to run this on startup.

Now, copy the file above to /home/pi/ and configure the device to run this automatically after boot up.

To do this, add the following new line:
(sleep 8;python3 /home/pi/piseesip.py)

to the file...
/etc/rc.local

This will run the python code in background upon startup after an 8 sec delay.
Runs as root so sudo command not required.
Now reboot the device.

### Expected Result

If you have the SenseHat installed and you have followed instructions above, you should be able to see a scrolling display of the wlan IP address simply by pressing the joystick button (any direction). It will display the IP scrolling twice. You can now connect via ssh on the same network.
