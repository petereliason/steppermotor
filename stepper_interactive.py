# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
control_pins = [17,22,23,24]

# Set all pins as output
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

# Define advanced sequence
# as shown in manufacturers datasheet
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]



delay = input("Time Delay (ms)?")  #maybe 10 to start.  1 works pretty good.
fsteps = input("How many steps forward? ")   #512 is once around

bsteps = input("How many steps backwards? ")

#sleeptime = input("sleep time? ")  #0.001 is default

delaydec= int(delay) / 1000.0
print(delaydec)

for i in range(int(fsteps)):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(delaydec)
    
    
for i in range(int(bsteps)):
  for halfstep in reversed(range(8)):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(delaydec)
    
GPIO.cleanup()

