import tkinter as tk
from Arduino import *

class MyArduino(Arduino):
    def arduino_done(self):
        #self.blink()
        text.insert('end', "DONE")

arduino = MyArduino(port="COM4")
arduino.connect()

def onKeyPress(event):
    key = ord(event.char);
    if key == 32:  # space
        arduino.connect()
        if(arduino.is_open()): text.insert('end', "Connected")
        else: text.insert('end', "Not connected")
    if key == 27:  # ESC
        text.insert('end', "Disconnecting")
        arduino.disconnect()
    elif key == 13:  # Enter
        text.insert('end', "Blinking")
        arduino.blink()

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
text.insert('end', 'Press enter to blink. Escape to disconnect. Space to connect')
root.mainloop()