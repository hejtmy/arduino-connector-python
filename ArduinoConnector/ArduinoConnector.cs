using System;
using System.IO.Ports;

namespace ArduinoConnector
{
    public enum ArduinoType {Leonardo, Uno, Generic}

    public class Arduino
    {

        private SerialPort _port;
        private string _comPort;

        private ArduinoType _arduinoType;

        public string ComPort => _comPort;
        public Arduino(ArduinoType type)
        {
            _arduinoType = type;
        }

        #region PUBLIC API
        /// <summary>
        /// Loops through open serial ports and tries to connect to arduino sketch
        /// </summary>
        /// <returns></returns>
        public bool Connect()
        {
            _port = TryPorts();
            if (IsOpen()) _comPort = _port.PortName;
            return IsOpen();
        }
        public string ReadMessage()
        {
            if (IsOpen()) return _port.ReadLine();
            return null;
        }
        public bool IsOpen()
        {
            if (_port != null && _port.IsOpen) return true;
            return false;
        }
        /// <summary>
        /// Closes the port while maintaining class settings
        /// </summary>
        public void Disconnect()
        {
            Restart();
            if (IsOpen()) _port.Close();
        }
        public void Restart()
        {
            if (IsOpen())
            {
                _port.WriteLine("RESTART");
                return;
            }
            SerialPort port;
            string comPort;
            if (!String.IsNullOrEmpty(_comPort))
            {
                port = SetupConnection(_comPort);
                if (port.IsOpen)
                {
                    port.WriteLine("RESTART");
                    return;
                }
            }
            //otherwise we loop through all the way - will redo in the future.
            foreach (string portName in SerialPort.GetPortNames())
            {
                comPort = portName;
                port = SetupConnection(comPort);
                if (port.IsOpen)
                {
                    port.WriteLine("RESTART");
                }
            }
        }
        public void Blink()
        {
            if (IsOpen()) _port.WriteLine("BLINK");
        }
        #endregion
        #region PRIVATE
#region Establishing connection

        /// <summary>
        /// Loops through all open ports and tries to connect and get a response.
        /// </summary>
        /// <returns>Connection successful</returns>
        private SerialPort TryPorts()
        {
            if (IsOpen()) Disconnect();
            SerialPort port;
            string comPort;
            //firstly triels the last port it was connected to 
            if (!String.IsNullOrEmpty(_comPort))
            {
                port = SetupConnection(_comPort);
                if (TryArduinoConnect(port)) return port;
            }
            foreach (string portName in SerialPort.GetPortNames())
            {
                comPort = portName;
                port = SetupConnection(comPort);
                if (TryArduinoConnect(port)) return port;
                Disconnect();
            }
            return null;
        }
        bool TryArduinoConnect(SerialPort port)
        {
            try
            {
                port.Open();
                if (ListenForConnectionMessage(port)) return true;
            }
            catch
            {
                Console.WriteLine("There was an error. Please make sure that the correct port was selected and the device, plugged in.");
            }
            return false;
        }
        /// <summary>
        /// Opens a specific connection - 
        /// </summary>
        /// <param name="portName"></param>
        /// <returns></returns>
        private SerialPort SetupConnection(string portName)
        {
            SerialPort port = new SerialPort(portName, 9600);
            if (_arduinoType == ArduinoType.Leonardo)
            {
                port.DtrEnable = true;
                port.RtsEnable = false;
            }
            return port;
        }
        /// <summary>
        /// Sends "WHO" to arduino and listens for answer "ARDUNIO". The timeout is set to be 50ms.
        /// </summary>
        /// <returns>true = "ARDUINO" retured</returns>
        /// <returns>false = something else or nothing retured</returns>
        private bool ListenForConnectionMessage(SerialPort port)
        {
            string info;
            port.WriteLine("WHO");
            try
            {
                port.ReadTimeout = 50;
                info = port.ReadLine();
            }
            catch (TimeoutException)
            {
                Console.WriteLine("Message was sent but no response came back. ");
                return false;
            }
            if (info.Contains("ARDUINO"))
            {
                SendDone(port);
                return true;
            }
            return false;
        }
        /// <summary>
        /// Ends the arduino loop waiting for connection confirmation
        /// </summary>
        private void SendDone(SerialPort port)
        {
            port.WriteLine("DONE");
        }
        #endregion
#endregion
    }
}
