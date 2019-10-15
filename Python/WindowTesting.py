import tkinter as tk
from Arduino import *

class MyArduino(Arduino):
    def arduino_done(self):
        #self.blink()
        text.insert('end', "DONE")

arduino = MyArduino(port="COM6", model=ArduinoModel.Nano)
arduino.connect()

def onKeyPress(event):
    key = ord(event.char)
    if key == 32:  # space
        arduino.connect()
        if(arduino.is_open()): text.insert('end', "Connected")
        else: text.insert('end', "Not connected")
    if key == 27:  # ESC
        text.insert('end', "Disconnecting")
        arduino.disconnect()
    if key == 13:  # Enter
        text.insert('end', "Blinking")
        arduino.blink()
    if key == 83: #s
        text.insert('end', "PULSING")
        arduino.send_pulse_up()
    if key == 75: #k
        text.insert('end', "STOPPING")
        arduino.send_pulse_down()

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
text.insert('end', 'Press enter to blink. Escape to disconnect. Space to connect')
root.mainloop()