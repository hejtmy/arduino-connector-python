import serial
import time
ser = serial.Serial('COM5', baudrate=38400, timeout=1, rtscts=False, dsrdtr=False)  # open serial port
print('waiting for clean connection')
time.sleep(3)
print('starting testing')
for i in ['k', 'kk', 'kkk', 'kkkk', 'kkkkk']:
  t = time.time()
  message = i + '!'
  ser.write(message.encode())
  s = ser.readline()
  print(s)
  print(time.time() - t)
  time.sleep(1)
ser.close() # close port