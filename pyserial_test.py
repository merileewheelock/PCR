# To print available ports: python -m serial.tools.list_ports

import serial
ser = serial.Serial('/dev/tty.usbmodem1421')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port