from Stepper import *
from PCF8591 import *
import json

light = Photoresistor(0x40)

try:
    while True:
        with open('/usr/lib/cgi-bin/stepperControlDump.txt','r') as f: #open data dump file
            data = json.load(f)
            selection = data['selection'] #selection input decides weather going to 0 or angle
            angle = int(data['angle'])
            if selection == 'Zero': #if for if zero was submit
                light.getLight()
                print('{:>3}'.format(light.Light))
    
except Exception as e: #exception error to print error and line number
    print('Error in the code')
    print(e)
    print(e.format_exc())
    GPIO.cleanup()
