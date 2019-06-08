#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial
import sys
import json
import paho.mqtt.publish as publish
reload(sys)
sys.setdefaultencoding('utf-8')
topic = 'th'
hostname = '45.76.53.193'
 
ser = serial.Serial(
	port = '/dev/serial0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)
 
print("Raspberry's receiving : ")
 
try:
    
    while True:
        s = ser.readline()
        print(s)
        if '{' in s:
            publish.single(topic, s, hostname=hostname)

 
except KeyboardInterrupt:
	ser.close()
