from network import LoRa
import socket
import machine
import time
import messageLoRa
from messageLoRa import messageLoRa
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
    global tryDiscover
    global discovered
    global myLoRa
    print("PHASE NOT DISCOVERED STARTED "+str(tryDiscover))
    s.send('Discover,'+str(1)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(-1)+','+str(-1))
    print("Discover sent by "+str(id))
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "Accept":
        myLoRa=msg.id_src
        print("Receive ACCEPT msg")
        discovered=True
    tryDiscover+=1
    time.sleep(slot)
    print("PHASE NOT DISCOVERED ENDED\n")
def notRegistered():
    #send some data
    global tryRegister
    global registered
    global myLoRa
    print("PHASE NOT REGISTERED STARTED\n")
    s.send('Register,'+str(3)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(-1))
    print("Register sent")
    # get any data received...
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "DataReq" and msg.id_src== myLoRa:
        registered=True
    else:
        tryRegister+=1
        time.sleep(slot)
    print("PHASE NOT REGISTERED ENDED\n")
def sendData():
    #send some data
    global tryDataReq
    global data
    global myLoRa
    global id
    global slots
    global frequency
    print("PHASE SEND DATA STARTED\n")
    s.send('DataRes,'+str(5)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data))
    print("DataResponse sent")
    #data_r=s.recv(128)
    #msg =messageLoRa()
    #msg.fillMessage(data_r)
    #if msg.messageName == "ack" and msg.id_src== myLoRa:
    #    ack_Data=True
    #else:
    #    tryDataReq+=1
    #    time.sleep(slot)
    print("PHASE SEND DATA ENDED\n")
while True:
    #We are not discovered yet
    while not discovered:
        notDiscovered()
    while not registered and discovered:
        notRegistered()

    dataR=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(dataR)
    if msg.kind=="4":
        sendData()
        print("I sent my data")
    data+=1
    time.sleep(slot)
