using System;
using System.Diagnostics;
using System.IO.Ports;
using System.Threading;
using System.Threading.Tasks;

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

        public void Disconnect()
        {
            if (_port != null && _port.IsOpen)
            {
                _port.Close();
            }
        }

        private bool ListenForMessage()
        {
            string info;
            _port.WriteLine("111");
            try
            {
                WaitForLine();
                _port.ReadTimeout = 1500;
                info = _port.ReadLine();
                Console.WriteLine(info);
            }
            catch (TimeoutException)
            {
                return false;
            }
            return info.Contains("666");
        }

        private void WaitForLine()
        {
            Thread.Sleep(200);
        }

        public string TakeReading()
        {
            SerialPort port = SetupConnection("COM5");
           
            string info;
            try
            {
                port.Open();
                port.ReadTimeout = 200;
                info = port.ReadLine();
                Console.WriteLine(info);
                port.Close();
            }
            catch (Exception e)
            {
                port.Close();
                return "nothing";
            }
            return info;
        }
    }
}
