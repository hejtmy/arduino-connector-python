using System;
using System.IO.Ports;
using System.Threading;

namespace ArduinoConnector
{
    public class Arduino
    {
        private SerialPort _port;
        private string _comPort;

        public string ComPort => _comPort;

        public bool TryConnect()
        {
            foreach (string portName in SerialPort.GetPortNames())
            {
                _comPort = portName;
                _port = SetupConnection(_comPort);
                try
                {
                    _port.Open();
                    var isArduino = ListenForMessage();
                    if (isArduino) return true;
                }
                catch
                {
                    Console.WriteLine(
                        "There was an error. Please make sure that the correct port was selected, and the device, plugged in.");
                }
                Disconnect();
            }
            return false;
        }

        private SerialPort SetupConnection(string portName)
        {
            SerialPort port = new SerialPort(portName, 9600);
            port.DtrEnable = true;
            port.RtsEnable = false;
            return port;
        }

        public string ReadMessage()
        {
            if (IsOpen())
            {
                return _port.ReadLine();
            }
            return null;
        }

        public bool IsOpen()
        {
            if (_port != null && _port.IsOpen) return true;
            return false;
        }

        public void Disconnect()
        {
            if (_port != null && _port.IsOpen) _port.Close();
        }

        private bool ListenForMessage()
        {
            string info;
            _port.WriteLine("WHO");
            try
            {
                //WaitForLine();
                _port.ReadTimeout = 50;
                info = _port.ReadLine();
                Console.WriteLine(info);
            }
            catch (TimeoutException)
            {
                return false;
            }
            return info.Contains("ARDUINO");
        }

        private void WaitForLine()
        {
            Thread.Sleep(10);
        }

        public void Blink()
        {
            if (IsOpen())
            {
                _port.WriteLine("BLINK");
            }
        }
    }
}
