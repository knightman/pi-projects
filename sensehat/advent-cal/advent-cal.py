# This file is modified from the published starter code example
# advent-cal.py
import datetime
from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()
sense.clear()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {

  'r' : [255, 0, 0],
  'o' : [255,165,0],
  'y' : [255,255,0],
  'g' : [0,128,0],
  'b' : [0,0,255],
  'i' : [75,0,130],
  'v' : [238, 130,238],
  'n' : [135, 80, 22],
  'w' : [255, 255, 255],
  'e' : [0, 0, 0]  # e stands for empty/black

}

# Pictures
with open('pictures.txt', 'r') as f:
  all_pics = f.readlines()

# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
# Display a given picture string on the sense HAT
# ------------------------------------------------
def display_pic(pic_string):

  # Get rid of newline and split the line into a list
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  # Look up each letter in the dictionary of colours and add it to the list
  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])

  # Display the pixel colours from the file
  sense.set_pixels(pic_list)

# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
while(True):
  event = sense.stick.wait_for_event()
  if event.action == 'pressed':
    sense.clear()
    current_day = int(datetime.date.today().strftime("%d"))
    display_pic(all_pics[current_day])
    sleep(5)
    sense.show_message(str(25-current_day) + ' days until Christmas!')
  sleep(1)
