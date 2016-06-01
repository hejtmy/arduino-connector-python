# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:26:38 2016
@author: Smoothie
"""

import serial
import time
import sys
from helpers import serial_ports

class Arduino():
    def __init__(self, port="COM5", baudrate=9600, timeout=0.01):
        self.arduinoConnection = serial.Serial()
        self.arduinoConnection.port = port
        self.arduinoConnection.timeout = timeout
        self.arduinoConnection.baudrate = baudrate
    def connect(self):
        if (isOpen()): return (True);
        try:
            connection = self.tryPorts();
        except Exception as ex:
            print("Couldn't connect to arduino!")
            print(ex)
        if(connection):
            self.arduinoConnection = connection
            self.sendPrepared()
    ### CONNECTION PART
    def tryPorts(self):
        if(self.isOpen()): self.disconnect();
        if(self.arduinoConnection.port != ""):
            if(self.tryConnect(self.arduinoConnection.port)): return connection
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
        connection.open()
        if(connection.is_open):
            if(self.testConnection(connection)): return connection
        else: return False
    def testConnection(self,connection):
        connection.timeout = 50;
        connection.write(b'WHO!')
        line = connection.readline();
        if("ARDUINO" in line):
            return True
        else:
            return False
    def isOpen(self):
        return(self.arduinoConnection.isOpen)
    def disconnect(self):
        if(self.isOpen()):
            self.restart()
            self.arduinoConnection.close()
    def reset(self):
        if (self.arduinoConnection.isOpen()):
            self.sendMessage("RESET")
    def blink(self):
        self.sendMessage("BLINK")
    def sendPrepared(self):
        self.sendMessage("DONE")
    def sendMessage(self,message):
        message = message + "!"
        byteMessage = str.encode(message)
        #bytearray(message,"utf-8")
        self.arduinoConnection.write(message)