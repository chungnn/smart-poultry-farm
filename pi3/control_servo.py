pi@raspberrypi:~ $ cd Desktop/
pi@raspberrypi:~/Desktop $ nano chicken_farm_monitor.py 
pi@raspberrypi:~/Desktop $ cat chicken_farm_monitor.py 
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
import time
import serial


OPEN = 'CMD:OPEN'
CLOSE = 'CMD:CLOSE'
TOPIC = 'feeding'
HOSTNAME = '45.76.53.193'
 
ser = serial.Serial(
	port = '/dev/serial0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)
 
def on_connect(mqttc, obj, flags, rc):
 pass
 
def on_message(mqttc, obj, msg):
 print(msg.topic + ' ' + str(msg.qos) + ' ' + str(msg.payload))
 if(msg.topic == TOPIC):
   if(str(msg.payload) == '1'):
    ser.write(OPEN)
    ser.flush()
   elif(str(msg.payload) == '0'):
    ser.write(CLOSE)
    ser.flush()
 
def on_publish(mqttc, obj, mid):
 print('mid: ' + str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
 pass
 
def on_log(mqttc, obj, level, string):
 pass
 
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
mqttc.connect(HOSTNAME, 1883, 60)
mqttc.subscribe(TOPIC, 0) 
mqttc.loop_forever()