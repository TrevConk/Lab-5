import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
        


state = 0

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
    #direction +/- one + -> ccw - -> cw
    state += dir
    if state > 7:
        state = 0
    elif state < 0:
        state = 7
    for pin in range(4):    # 4 pins that need to be energized
        GPIO.output(pins[pin], dir[halfstep][pin])

def moveSteps(steps, dir):
    for step in steps:
        halfstep(dir)

while True:
    halfstep(1)
# Commented out because implemented into stepper_control_back

#try:
#  loop(cw)
#  loop(ccw)
#except:
#  pass
#GPIO.cleanup() 