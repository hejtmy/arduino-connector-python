using System;
using ArduinoConnector;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace TestingConnector
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            var arduino = new Arduino();
            arduino.TryConnect();
        }
    }
}
