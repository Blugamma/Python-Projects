from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("COM5",9600,timeout=2)
board.readall()
randomID = random()
client = Mosquitto("OllieSmith" + str(randomID))
client.connect("10.212.61.136")
print("connected")

#Subscribe to the "/lights" topic
client.subscribe("/lights")

    #Write a function to handle the incoming message
def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    board.write(payload.encode()+'\n')
    print("Message " + msg.topic + " containing: " + payload)
    #client = None
    
    #Register the incoming message handler
client.on_message = messageReceived

    #While the client still exists, ask it to process incoming messages
while (client != None): client.loop()



