Adruino connector for unity is a windows .net dll library for your projects that allows communication between your software and arduino through serial port communication.It is capable to search for arduino, reset connections and send cutom messages there and back. The main part are the ArduinoConnector which has the c# written connector and the Main folder which hosts the .ino file to be uploaded.

Two other projects are testers for the dll.

#How to work with this
1. Upload .ino to the arduino.
2. Add the dll to your project.
3. Instantiate Arduino class
  ```c#
  var arduino = new ArduinoConnector(ArduinoType.Leonardo)
  if(arduino.Connect()) Debug.Log('Connects');
  ```

4. Play with it
  ```c#
  arduino.Blink();

  void PrintLine(ArduinoEvent arduinoEvent){Console.Write(arduinoEvent.ToString());};
  arduino.DataIncomming += PrintLine;

  adruino.SendPulse(true);
  adruino.SendPulse(false);
  ```

5. Disconnect
  ```c#
  arduino.Disconnect();
  ```
