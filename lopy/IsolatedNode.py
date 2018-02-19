from network import LoRa
import socket
import machine
import time
import messageLoRa
from messageLoRa import messageLoRa  # means YourClass.py
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

id=1
timer=0
data=0
tryDiscover=0
tryRegister=0
discovered=False
registered=False
ack_Data=False
frequency=1.0
old_phase=frequency
slot=1
myLoRa=-1
tryDataReq=-1


def notDiscovered():
    #send some data
    s.send('Discover,'+str(frequency)+','+str(slot)+','+str(id)+','+str(-1)+','+str(-1))
    print("Discover sent by "+str(id))
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "Accept":
        myLoRa=msg.id_src
    #Something understandable ? Accept message? anything else ?
    # wait a random amount of time
    time.sleep(machine.rng() & 0x0F)

def notRegistered():
    #send some data
    s.send('Register,'+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(-1))
    print("Register sent")
    # get any data received...
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "DataReq" and msg.id_src== myLoRa:
        registered=True
    else:
        tryRegister+=1
        time.sleep(machine.rng() & 0x0F)
def sendData():
    #send some data
    s.send('DataRes,'+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data))
    print("DataResponse sent")
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "ack" and msg.id_src== myLoRa:
        ack_Data=True
    else:
        tryDataReq+=1
        time.sleep(machine.rng() & 0x0F)

while True:
    #We are not discovered yet
    while not discovered:
        notDiscovered()
    while not registered and discovered:
        notRegistered()
    while not ack_Data :
        sendData()
    data+=1
    time.sleep(slot)
