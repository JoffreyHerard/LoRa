from network import LoRa
import socket
import machine
import time
from messageLoRa import messageLoRa
from machine import Timer




#frequency accepts values between 863000000 and 870000000
#FROM SPEC LORAWAN LORA
#868000000 F1
#868100000 F2
#868300000 F3
#868500000 F4
#864100000 F5
#864300000 F6
#864500000 F7
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
    else:
        print("FREQUENCY ALREADY CHANGED")


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
        if isListening:
            isListening=False
def notDiscovered():
    #send some data
    global tryDiscover
    global discovered
    global myLoRa
    print("PHASE NOT DISCOVERED STARTED "+str(tryDiscover))
    s.send('Discover,'+str(1)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(-1)+','+str(-1)+','+str(-1))
    print("Discover sent by "+str(id))
    data=s.recv(128)
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "Accept":
        myLoRa=msg.id_src
        frequency=msg.frequency
        change_frequency(msg.frequency)
        print("Receive ACCEPT msg")
        discovered=True
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
    if msg.messageName == "DataReq" and msg.id_src== myLoRa:
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
    global slots
    global frequency
    print("PHASE SEND DATA STARTED\n")
    s.send('DataRes,'+str(5)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data)+','+str(-1))
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
clock = TimerL(slot)


while True:
    if isListening:
        #We are not discovered yet
        while not discovered:
            notDiscovered()
            time.sleep(machine.rng())
        while not registered and discovered:
            notRegistered()
            time.sleep(machine.rng())

        dataR=s.recv(128)
        msg =messageLoRa()
        msg.fillMessage(dataR)
        if msg.kind=="4":
            sendData()
            clock = TimerL(msg.listeningtime)
            print("I sent my data")
        data+=1
    else:
        #I will sleep
        print ("I SLEEP OK ! LET ME SLEEP IN PEACE")
        time.sleep(slot)
        isListening=True
