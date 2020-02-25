# import paho mqtt
import paho.mqtt.client as mqtt


# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime
#now = datetime.datetime.now()
def on_publish(client,userdata,result):             #create function for callback
    print("data submitted")
    pass

# definisikan nama broker yang akan digunakan
broker = "192.168.1.2"

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")

client.on_publish=on_publish

# koneksi ke broker
print("connecting to broker")
client.connect(broker, port=3333)


# mulai loop client
client.loop_start()
# lakukan 20x publish waktu dengan topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)

    # publish waktu sekarang
    waktu = datetime.datetime.now()
    #print("Publishing message to topic","waktu")
    client.publish("waktu", str(waktu)+" "+ str(i))
	
#stop loop
client.loop_stop()
