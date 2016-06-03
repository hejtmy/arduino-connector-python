from Arduino import *

arduino = Arduino(port="COM4")
arduino.connect()
print(arduino.is_open())
arduino.blink()
arduino.disconnect()