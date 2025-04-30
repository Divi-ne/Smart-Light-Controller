import time
from datetime import datetime
import paho.mqtt.publish as publish
# Set the times to send ON and OFF (24-hour format)
ON_TIME = "16:59"
OFF_TIME = "17:00"
# MQTT settings
MQTT_BROKER = "157.173.101.159"
TOPIC = "relay/controll"
sent_on = False
sent_off = False
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == ON_TIME and not sent_on:
        publish.single(TOPIC, payload="ON", hostname=MQTT_BROKER)
        print("Sent ON")
        sent_on = True
    if current_time == OFF_TIME and not sent_off:
        publish.single(TOPIC, payload="OFF", hostname=MQTT_BROKER)
        print("Sent OFF")
        sent_off = True
    time.sleep(1)

