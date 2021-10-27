import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

class Photoresistor:
  
  def __init__(self,address):
    self.adc = PCF8591(0x48)

  def getLight(self):
    self.Light = self.adc.read(0)

light = Photoresistor(0x40)

try:
  while(True):
    light.getLight()
    print('{:>3}'.format(light.Light))
    time.sleep(.1)
except Exception as e:
  print(e)
  
