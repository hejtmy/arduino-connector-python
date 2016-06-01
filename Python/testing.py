from Arduino import *

arduino = Arduino(port="COM4")
arduino.connect()
print(arduino.isOpen())
arduino.blink()
arduino.disconnect()