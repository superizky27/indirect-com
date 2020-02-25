# import paho mqtt
import paho.mqtt.client as mqtt


# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime
#now = datetime.datetime.now()
#def on_publish(client,userdata,result):             #create function for callback
#    print(str(now))
#    pass

# definisikan nama broker yang akan digunakan
broker = "127.0.0.1"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P1")

#client.on_publish=on_publish

# koneksi ke broker
print("connecting to broker")
client.connect(broker, port=1883)


# mulai loop client
client.loop_start()
print("Subscribing to topic","house/bulbs/bulb1")
# lakukan 20x publish waktu dengan topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)

    # publish waktu sekarang
    waktu = datetime.datetime.now()
    print("Publishing message to topic","waktu")
    client.publish("waktu","OFF")
	
#stop loop
client.loop_stop()
