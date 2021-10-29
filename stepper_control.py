#!/usr/bin/python37all
import cgi
import cgitb
import json

cgitb.enable(display=1)
data = cgi.FieldStorage()

value = 0

if value in int(data.getvalue('angleText')):
    angle = value
else:
    angle = int(data.getValue('angleRange'))

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
print('<input type="range" name="angleRange" min="0" max="180" value="%s"><br>' % angle)
print('''
    <input type="text" name="angleText"><br>
    <input type="submit" name="submit" value="Zero"><br>
    <input type="submit" name="submit" value="Submit"><br>
    </input>
</form>
</html>''')