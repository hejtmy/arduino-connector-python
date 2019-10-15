from Arduino import *

arduino = Arduino(port="COM6", model=ArduinoModel.Nano)
arduino.connect()
print(arduino.is_open())
arduino.blink()
arduino.disconnect()