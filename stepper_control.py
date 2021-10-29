#!/usr/bin/python37all
import cgi
import cgitb
import json

cgitb.enable(display=1)
data = cgi.FieldStorage()

value = 0

#if data.has_key('angleText'):
#    angle = data.getvalue('angleText')
#else:

if data.getvalue('angleText') is not None:
    angle = data.getvalue('angleText')
else:
    angle = data.getvalue('angleRange')



selection = data.getvalue('submit')

dataDump = {'angle':angle,'selection':selection}
with open('stepperControlDump.txt', 'w') as f:
  json.dump(dataDump, f)

if selection == 'zero': #set angle to zero for processing the webpage
    angle = 0

print('Content-type: text/html\n\n')
print('''
    <html>
    <form action="/cgi-bin/stepper_control.py" method="POST">''')
print('<b>Current Angle: %s</b><br>' %angle)
print('<b>Use Range to Input Angle</b>')
print('<input type="range" name="angleRange" min="0" max="360" value="%s"><br>' % angle)
print('''
    <b>Use Slider to Input Angle</b>
    <input type="text" name="angleText"><br>
    <input type="submit" name="submit" value="Zero"><br>
    <input type="submit" name="submit" value="Submit"><br>
    </input>
</form>
</html>''')