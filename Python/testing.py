from Arduino import *

arduino = Arduino()
arduino.connect()
print(arduino.isOpen())
arduino.blink()
arduino.disconnect()