import tkinter as tk
from Arduino import *
arduino = Arduino(port="COM4")
arduino.connect()

def onKeyPress(event):
    key = ord(event.char);
    if key == 27:  # ESC
        text.insert("Disconnecting")
        arduino.disconnect()
    elif key == 13:  # Enter
        text.insert("Blinking")
        arduino.blink()
    text.insert('end', 'You pressed %s\n' % (event.char))

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()