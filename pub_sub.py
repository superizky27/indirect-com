# gunakan library paho mqtt
import paho.mqtt.client as mqtt

# library untuk sleep
import time

# callback: fungsi yang akan dipanggil jika message di buffer
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
    
# alamat broker yang akan digunakan    
broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# pada client dikaitkan callback function
client.on_message=on_message

# client terkoneksi dengan broker
print("connecting to broker")
client.connect(broker_address, port=1883)

# client P1 mulai
client.loop_start()

# client P1 subscribe ke topik "house/bulbs/bulb1"
# P1 <- broker
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")

# client P1 publish ke broker dengan topik "house/bulbs/bulb1"
# P1 -> broker
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")

time.sleep(1)
client.loop_stop()
