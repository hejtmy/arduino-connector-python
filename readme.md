Adruino connector for unity is a windows .net dll library for your projects that allows communication between your software and arduino through serial port communication.It is capable to search for arduino, reset connections and send cutom messages there and back. The main part are the ArduinoConnector which has the c# written connector and the Main folder which hosts the .ino file to be uploaded.

Two other projects are testers for the dll.

#How to work with this
1. Upload .ino to the arduino.

2. Add the Arduino.py to your project
3. Instantiate Arduino class
  ```python
  arduino = Arduino()
  arduino.Connect()
  ```

4. Play with it
  ```python
  arduino.blink()
  arduino.send_pulse_up()
  arduino.send_pulse_down()
  ```

5. Disconnect
  ```python
  arduino.disconnect();
  ```

## Photoresistor functionality
  
## Threading
If you want to use the threading capabilities there are some more advanced changes needed. Mainly you need to change the arduino class to include your own implementation of threaded methods.

```python
	arduino = Arduino(threading = True)
```

###Methods
These are some of the methods that you can override to achieve needed functionality
#### arduino done
```python
	class MyArduino(Arduino):
		def arduino_done(self):
			print("I am done")
```