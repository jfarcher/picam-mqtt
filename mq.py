#!/usr/bin/python

import mosquitto
import picamera
import time

#define what happens after connection
def on_connect(rc):
   print "Connected"

def on_message(msg):

    print (msg.payload)
    with picamera.PiCamera() as camera:
    	camera.start_preview()
    	camera.capture('/var/www/cam.jpg')
	camera.stop_preview()
	
mqttc = mosquitto.Mosquitto("doorbell_cam")

#define the callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect

#connect
mqttc.connect("192.168.1.3", 1883, 60, True)

#subscribe to topic 
mqttc.subscribe("house/doorbell", 2)

#keep connected to broker
while mqttc.loop() == 0:
    pass


