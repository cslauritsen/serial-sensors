#!/usr/bin/env python3
import serial
import config


#PORT = '/dev/arduino-serial'
PORT = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_7543331373935161D021-if00'
BAUD = 115200
TIMEOUT = 10
ser = None

try:
    cfg = config.Config()
    cfg.validate()
    ser = serial.Serial(cfg['serial']['port'], baudrate=BAUD, timeout=TIMEOUT)
    print('Opened', ser)
    while(True):
        ba = ser.read(10)
        s = ba.decode('ascii')
        print("read string:", s)
finally:
    ser.close()
    print()
    print("Closed serial port")


