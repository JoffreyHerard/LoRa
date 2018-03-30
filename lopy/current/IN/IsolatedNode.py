from network import LoRa
import socket
import machine
import uos
import time
import pycom
import messageLoRa
from messageLoRa import messageLoRa
from machine import Timer

pycom.heartbeat(False)
def Random():
    result = ((uos.urandom(1)[0] / 256 )*3)+2
    return result
def change_frequency(frequency_d):
    current_frequency=lora.frequency()
    if current_frequency != frequency_d:
        print("FREQUENCY WAS CHANGED FROM :"+str(current_frequency)+" TO= ")
        if frequency_d == 1:
            lora.frequency(868000000)
            print("868000000")
        if frequency_d == 2:
            lora.frequency(868100000)
            print("868100000")
        if frequency_d == 3:
            lora.frequency(868300000)
            print("868300000")
        if frequency_d == 4:
            lora.frequency(868500000)
            print("868500000")
        if frequency_d == 5:
            lora.frequency(864100000)
            print("864100000")
        if frequency_d == 6:
            lora.frequency(864300000)
            print("864300000")
        if frequency_d == 7:
            lora.frequency(864500000)
            print("864500000")
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
id=1
timer=0
data=42
tryDiscover=0
tryRegister=0
discovered=False
registered=False
ack_Data=False
frequency=1.0
old_phase=frequency
slot=10
myLoRa=-1
tryDataReq=-1
isListening=True

class TimerL:
    def __init__(self,timing):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, timing, periodic=True)
    def _seconds_handler(self, alarm):
        global isListening
        alarm.cancel() # stop it
        if isListening:
            isListening=False
def notDiscovered():
    global tryDiscover
    global discovered
    global myLoRa
    global id
    global frequency
    global slot
    print("PHASE NOT DISCOVERED STARTED "+str(tryDiscover))
    s.send('Discover,'+str(1)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(-1)+','+str(-1)+','+str(-1))
    print("Discover sent by "+str(id))
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    print("dest ==="+str(msg.get_dest()))
    if msg.messageName == "Accept" and msg.id_dest == str(id):
        myLoRa=msg.id_src
        frequency=msg.frequency
        change_frequency(msg.frequency)
        print("Receive ACCEPT msg")
        discovered=True
    else:
        time.sleep(1)
    tryDiscover+=1
    print("PHASE NOT DISCOVERED ENDED\n")
def notRegistered():
    #send some data
    global tryRegister
    global registered
    global myLoRa
    print("PHASE NOT REGISTERED STARTED\n")
    s.send('Register,'+str(3)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(-1)+','+str(-1))
    print("Register sent")
    # get any data received...
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "DataReq" and msg.id_src== myLoRa and msg.id_dest == str(id):
        registered=True
    else:
        tryRegister+=1
    print("PHASE NOT REGISTERED ENDED\n")
def sendData():
    #send some data
    global tryDataReq
    global data
    global myLoRa
    global id
    global slot
    global frequency
    print("PHASE SEND DATA STARTED\n")
    print('DataRes,'+str(5)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data)+','+str(70))
    s.send('DataRes,'+str(5)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data)+','+str(70))
    #time.sleep(20)
    print("DataResponse sent")
    print("PHASE SEND DATA ENDED\n")
while True:
    if isListening:
        #print("I am awake : my LoRaGW is "+str(myLoRa)+" and my slot is "+str(slot))
        pycom.rgbled(0x007f00) # green
        #We are not discovered yet
        while not discovered:
            notDiscovered()
            rnd=Random()
            print("Try Discover in "+str(rnd))
            time.sleep(rnd)
        while not registered and discovered:
            notRegistered()
            rnd=Random()
            print("Try Register in "+str(rnd))
            time.sleep(rnd)
        dataR=s.recv(128)
        msg =messageLoRa()
        msg.fillMessage(dataR)
        if msg.kind=="4" and msg.id_dest == str(id):
            sendData()
            slot=int(msg.listeningtime)
            clock = TimerL(float(msg.listeningtime))
            print("I sent my data")

    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        del clock
        time.sleep(slot)
        isListening=True
        clock = TimerL(slot)
