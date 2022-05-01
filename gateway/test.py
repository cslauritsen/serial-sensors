#!/usr/bin/env python3
import serial

#PORT = '/dev/arduino-serial'
PORT = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_7543331373935161D021-if00'
BAUD = 115200
TIMEOUT = 10
ser = None

try:
    ser = serial.Serial(PORT, baudrate=BAUD, timeout=TIMEOUT)
    print('Opened', ser)
    while(True):
        ba = ser.read(10)
        s = ba.decode('ascii')
        print("read string:", s)
finally:
    ser.close()
    print()
    print("Closed serial port")


