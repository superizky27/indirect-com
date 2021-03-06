# import paho mqtt
import paho.mqtt.client as mqtt


# import time for sleep()
import time


# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # print pesan 
	print("message received " ,str(message.payload.decode("utf-8")))



########################################
    
# buat definisi nama broker yang akan digunakan
broker = "192.168.1.3"


# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker, port=3333)
print("connected!")

# jalankan loop client
client.loop_start()


# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic1 and topic12")
client.subscribe([("topik1",0),("topik2",0)])

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()
