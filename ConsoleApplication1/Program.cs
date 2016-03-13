using System;
using System.IO.Ports;
using System.Timers;

namespace ConsoleApplication1
{
    class Program
    {

        private static SerialPort port;

        static void Main(string[] args)
        {
            Setup();

            Timer myTimer = new Timer();
            myTimer.Elapsed += new ElapsedEventHandler(ReadData);
            myTimer.Interval = 1000;
            myTimer.Enabled = true;
            while (true)
            {
                
            }
        }

        private static void ReadData(object sender, EventArgs e)
        {
            string data = port.ReadLine();
            Console.WriteLine(data);
            Console.WriteLine(data.Contains("ARDUINO"));
        }
        private static void Setup()
        {
            port = new SerialPort("COM5", 9600);
            port.DtrEnable = true;
            port.RtsEnable = false;
            if (!port.IsOpen)
            {
                try
                {
                    port.Open();
                    port.WriteLine("WHO");
                }
                catch
                {
                    Console.WriteLine("There was an error. Please make sure that the correct port was selected, and the device, plugged in.");
                }
            }
        }
    }
}
