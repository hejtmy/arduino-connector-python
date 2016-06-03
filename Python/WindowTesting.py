import tkinter as tk
from Arduino import *
arduino = Arduino(port="COM4")
arduino.connect()

def onKeyPress(event):
    key = ord(event.char);
    if key == 32:  # space
        arduino.connect()
        if(arduino.isOpen()): text.insert('end', "Connected")
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
root.mainloop()

text.insert('end', 'Press enter to blink. Escaoe to disconnect. Space to connect')