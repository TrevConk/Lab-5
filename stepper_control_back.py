from Stepper import *
from PCF8591 import *
import json

light = Photoresistor(0x40)
currentAngle = 0

try:
    while True:
        with open('/usr/lib/cgi-bin/stepperControlDump.txt','r') as f: #open data dump file
            data = json.load(f)
            selection = data['selection'] #selection input decides weather going to 0 or angle
            angle = data['angle']
        if selection == 'Zero': #if for if zero was submit
            light.getLight()
            print('{:>3}'.format(light.Light))
            while(int('{:>3}'.format(light.Light)) < 220):
                light.getLight()
                moveSteps(8,1)
                print('{:>3}'.format(light.Light))
            currentAngle = 0
        elif selection == 'Submit' and currentAngle != angle:
            print(angle)
            steps = int((float(angle)-float(currentAngle))*8*512/360)
            print(steps)
            if(steps > 0):
                moveSteps(steps,1)
            else:
                moveSteps(abs(steps),-1)
            currentAngle = angle
        time.sleep(.1)


except Exception as e: #exception error to print error and line number
    print('Error in the code')
    print(e)
    GPIO.cleanup()
