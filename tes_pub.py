import paho.mqtt.client as paho
broker="127.0.0.1"
port=3333
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("house/bulb1","on")                   #publish