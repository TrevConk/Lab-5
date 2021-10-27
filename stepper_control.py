#!/usr/bin/python37all
import cgi
import cgitb
import json

cgitb.enable()
data = cgi.FieldStorage()

if value in data.getvalue('angleText'):
    angle = value
else:
    angle = data.getValue('angleRange')

selection = data.getvalue('submit')

Brightness = data.getvalue('BrightVal')
dataDump = {'angle':angle,'selection':selection}
with open('stepperControlDump.txt', 'w') as f:
  json.dump(dataDump, f)

if selection == 'zero': #set angle to zero for processing the webpage
    angle = 0

print('Content-type: text/html\n\n')
print('''
    <html>
    <form action="/cgi-bin/stepper_control.py" method="POST">''')
print('<b>Use Slider to Input Angle. Current angle = %s</b>' %angle)
print('<input type="range" name="angleRange" min="0" max="180" value="%s"><br>' % angle)
print('''
    <input type="text" name="angleText"><br>
    <input type="submit" name="submit" value="Zero"><br>
    <input type="submit" name="submit" value="Submit"><br>
    </input>
</form>
</html>''')