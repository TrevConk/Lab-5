from Stepper import *
from PCF8591 import *
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #GPIO SETUP

GPIO.setup(13, GPIO.OUT) #Establish LED on GPIO Pin 13


light = Photoresistor(0x40)
currentAngle = 0

try:
    while True:
        with open('/usr/lib/cgi-bin/stepperControlDump.txt','r') as f: #open data dump file
            data = json.load(f)
            selection = data['selection'] #selection input decides weather going to 0 or angle
            angle = data['angle']
        if selection == 'Zero': #if for if zero was submit
            GPIO.output(13, GPIO.HIGH) #Turn on LED
            light.getLight() 
            print('{:>3}'.format(light.Light))
            while(int('{:>3}'.format(light.Light)) < 200):
                light.getLight()
                zero()
                print('{:>3}'.format(light.Light))
            currentAngle = 0
            GPIO.output(13, GPIO.LOW)
        elif selection == 'Submit' and currentAngle != angle: #if submit was normal submit
            goAngle(angle, currentAngle)
            currentAngle = angle
            print(angle)
            print(currentAngle)
        time.sleep(.1)


except Exception as e: #exception error to print error and line number
    print('Error in the code')
    print(e)
    GPIO.cleanup()
