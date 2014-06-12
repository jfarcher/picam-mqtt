picam-mqtt
==========

picam-mqtt is a very simple python script which utilises the Raspberry Pi camera and MQTT. The script sits in a loop subscribed to a particular MQTT topic. if a payload comes in to that topic (no specifics at the moment) an image capture is triggered. This image is then placed in a particular location. In this case /var/www so can be viewed via a web browser.

On receipt of an mqtt payload take a still image with the Pi Camera

Prerequisites
=============
python-mosquitto
python-picamera (or python3-picamera)

for web presentation apache2 is also needed and rights for the user running the script to the output directory /var/www
To get it working
=================
You will need to modify both the MQTT broker address and the topic in the mq.py file. You may also wish to change the output folder from /var/www.

Run the script as follows

python mq.py

or if you wish to background the process

python mq.py &

