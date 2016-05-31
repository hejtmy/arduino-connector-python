# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:26:38 2016
@author: Smoothie
"""

import serial, time, msvcrt, sys

class Arduino():
    def __init__(self, port="COM5", baudrate=9600, timeout=0.01):
        self.arduinoConnection = serial.Serial()
        self.arduinoConnection.port = port
        self.arduinoConnection.timeout = timeout
        self.arduinoConnection.baudrate = baudrate
    def connect(self):
        if (isOpen()): return (true);
        port = self.tryPorts();
        try:
            self.arduinoConnection.open();
        except Exception as ex:
            print("Couldn't connect to arduino!")
            print(ex)
            msvcrt.getch()
            sys.exit(1)
    def tryPorts(self):
        if(self.isOpen()): self.disconnect();
        if(self.arduinoConnection.port != ""):
            if(self.tryConnect(self.arduinoConnection.port)): return

    def isOpen(self):
        return(self.arduinoConnection.isOpen)
    def disconnect(self):
        try:
            self.arduinoConnection.close()
        except Exception:
            print("Couldn't disconnect from arduino!")
    def flush(self):
        self.arduinoConnection.flushInput()
        self.arduinoConnection.flushOutput()
    def stopSending(self):
        if (self.arduinoConnection.isOpen() == True):
            self.arduinoConnection.write(b"STOP")
        else:
            print("Arduino is not connected!")
    def reset(self):
        if (self.arduinoConnection.isOpen()):
            self.sendMessage("RESET")
        else:
            print("Arduino is not connected!")
    def beep(self):
        self.arduinoConnection.write(b"BEEP")
    def prepare(self):
        if self.arduinoConnection.isOpen():
            self.arduinoConnection.read_all()

            while (True):
                while (self.arduinoConnection.inWaiting() == 0):
                    pass
                if (self.arduinoConnection.readline() == b"CX37"):
                    self.stopSending()
                    self.arduinoConnection.flushOutput()
                    self.arduinoConnection.flushInput()
                    break
        else:
            print("Arduino is not connected!")
    def isPushed(self):
        if (self.arduinoConnection.in_waiting > 0):
            #            before = time.clock()
            receivedText = self.arduinoConnection.readline()
            #            after = time.clock()
            #            print("Received text: ", receivedText, "Reading buffer took: %fs" %(after - before))
            if (receivedText == b"PUSHED"):
                return True
            else:
                print("Incorrect received text: ", receivedText)
                return False
    def sendMessage(self,message):
        message = message +"!"
        self.arduinoConnection.write(message)