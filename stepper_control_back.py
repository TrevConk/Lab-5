from Stepper import *
from PCF8591 import *
import json



try:
    while True:
        with open('/usr/lib/cgi-bin/stepperControlDump.txt','r') as f: #open data dump file
            data = json.load(f)
            selection = data['selection'] #selection input decides weather going to 0 or angle
            angle = int(data['angle'])
            if selection == 'Zero': #if for if zero was submit
                while(light.getLight() < 190): #check to see that the light is not blocked
                    print('turning')
    
except Exception as e: #exception error to print error and line number
    print('Error in the code')
    print(e)
    print(e.format_exc())
    GPIO.cleanup()
