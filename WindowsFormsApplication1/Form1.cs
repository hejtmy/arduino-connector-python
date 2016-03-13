using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ArduinoConnector;
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
       
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void TakeReading()
        {
            label1.Text = arduino.TakeReading();
        }

        private void Connect()
        {
            arduino.Disconnect();
            if (arduino.TryConnect()) label2.Text = "YES!";
            label1.Text = arduino.ComPort;
        }

        private void button1_Click(object sender, EventArgs e)
        {
           Connect();
        }
    }
}
