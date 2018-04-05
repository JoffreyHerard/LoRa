from network import LoRa
import socket
import time
import pycom
import uos
import messageLoRa
from machine import Timer
from messageLoRa import messageLoRa
pycom.heartbeat(False)
pycom.rgbled(0xff00)
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
id=2
timer=0
NbIN=0
idRegistered=[]
isRegistered=[]
frequency=1
discovered=False
old_phase=frequency
slot=10
MyLW=0
nb_harvest=0
mycolor="blue"
isListening=True



def Random():
    result = (uos.urandom(1)[0] / 256)*5
    return result
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
class TimerL:
    def __init__(self,timing):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, timing, periodic=True)

    def _seconds_handler(self, alarm):
        global isListening
        alarm.cancel() # stop it
        if isListening:
            isListening=False
def pairing_phase(msg):
    global slot
    global idRegistered
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('Accept,'+str(2)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    idRegistered.append(msg.id_src)
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" ENDED")
def registering_phase(msg):
    global isRegistered
    global slot
    #print("REGISTERING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    if msg.id_src in isRegistered:
        print("Added before")
    else:
        isRegistered.append(msg.id_src)
    #print("REGISTERING PHASE WITH "+str(msg.id_src)+" ENDED")
def ack_data(msg):
    #print("STANDARD PHASE STARTED")
    global slot
    #print("I received data : "+str(msg.data))
    s.send('ack,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    #print("STANDARD PHASE ENDED")
def standard():
    print("STANDARD PHASE STARTED")
    global isRegistered
    global slot
    for idDest in isRegistered:
        print(idDest)
        print('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot))
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot))

        dataHarvested = s.recv(128)
        msgH =messageLoRa()
        msgH.fillMessage(dataHarvested)
        rnd=Random()
        print("[FIRST Send] Request data in "+str(rnd))
        print(dataHarvested)
        time.sleep(rnd)
        while msgH.id_src != idDest and msgH.id_dest != id and msgH.kind != "5":
            rnd=Random()
            print("[Try] send Request data in "+str(rnd))
            time.sleep(rnd)
            s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot))
            dataHarvested = s.recv(128)
            msgH =messageLoRa()
            msgH.fillMessage(dataHarvested)
    print("STANDARD PHASE ENDED")
def handle_message(data):
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.kind == "1":
        pairing_phase(msg)
    #else:
        #print("not kind 1")
    if msg.kind == "3" and msg.id_dest == str(id):
        registering_phase(msg)
    #else:
    #    print("not kind 3")
    
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
clock = TimerL(slot)
while True:
    if isListening:
        print("I am awake")
        pycom.rgbled(0x007f00) # green
        data = s.recv(128)
        handle_message(data)
        standard()
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        isListening=True
        del clock
        clock = TimerL(slot)
