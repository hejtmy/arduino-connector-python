# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:26:38 2016
@author: Smoothie
"""

import serial
from helpers import serial_ports

class Arduino():
    def __init__(self, port="COM5", baudrate=9600, timeout=0.01):
        self.arduinoConnection = serial.Serial()
        self.arduinoConnection.port = port
        self.arduinoConnection.timeout = timeout
        self.arduinoConnection.baudrate = baudrate
    def connect(self):
        if (self.isOpen()): return (True);
        connection = self.tryPorts();
        if(connection):
            self.arduinoConnection = connection
            self.sendPrepared()
    ### CONNECTION PART
    def tryPorts(self):
        if(self.isOpen()): self.disconnect();
        if(self.arduinoConnection.port != ""):
            connection = self.tryConnect(self.arduinoConnection.port)
            if(connection): return connection
        ports = serial_ports(10);
        for port in ports:
            connection = self.tryConnect(port)
            if(connection): return connection
        return False
    def tryConnect(self,port):
        connection = serial.Serial()
        connection.port = port
        connection.rts = True
        connection.dtr = True
        connection.timeout = 0.05;
        try:
            connection.open()
        except Exception as ex:
            print("Couldn't connect to device at " + port)
            print(ex)
            return False
        if(self.testConnection(connection)): return connection

    def testConnection(self,connection):
        connection.write(b'WHO!')
        line = self.readline(connection);
        if("ARDUINO" in line):
            return True
        else:
            return False

    def readline(self,connection=None):
        if connection is None:
            connection = self.arduinoConnection
        try:
            line = connection.readline();
            return line.decode("utf-8");
        except Exception as ex:
            print(ex)
    def isOpen(self):
        return(self.arduinoConnection.isOpen())
    def disconnect(self):
        if(self.isOpen()):
            self.restart()
            self.arduinoConnection.close()
    def reset(self):
        if (self.isOpen()):
            self.sendMessage("RESET")
    def blink(self):
        if self.isOpen():
            self.sendMessage("BLINK")
    def sendPrepared(self):
        self.sendMessage("DONE")
    def sendMessage(self,message):
        message = message + "!"
        byteMessage = message.encode("utf-8")
        #bytearray(message,"utf-8")
        self.arduinoConnection.write(byteMessage)