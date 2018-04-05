from network import LoRa
import socket
import time
import pycom
import uos
import messageLoRa
import binascii
import struct
from machine import Timer
from messageLoRa import messageLoRa
pycom.heartbeat(False)
pycom.rgbled(0xff00)
id=3
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
listeningTime=10.0
def Random():
    result = ((uos.urandom(1)[0] / 256 )*3)+2
    return result
class TimerL:
    def __init__(self,timing,kind):
        self.seconds = 0
        if kind == 1:
            self.__alarm = Timer.Alarm(self._first_handler, timing, periodic=True)
        else:
            self.__alarm = Timer.Alarm(self._seconds_handler, timing, periodic=True)

    def _first_handler(self, alarm):
        global isListening
        alarm.cancel() # stop it
        isListening=True
    def _seconds_handler(self, alarm):
        global isListening
        alarm.cancel() # stop it
        isListening=False
def changetoA(s,dev_eui,app_key,app_eui,lora):
    print("CHANGE TO ANOTHER MEANS OF COMMUNICATING")
def changetoBluetooth(bluetooth):
    #lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
    print('Radio mode is Bluetooth now !')
    time.sleep(5)
def send_data(socket,dataString):
    print("SENDING DATA")
def pairing_phase(msg):
    global slot
    global idRegistered
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('Accept,'+str(2)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot*3))
    if msg.id_src in idRegistered:
        print("Added before")
    else:
        idRegistered.append(msg.id_src)
    #print("PAIRING PHASE WITH "+str(msg.id_src)+" ENDED")
def registering_phase(msg):
    global isRegistered
    global slot
    #print("REGISTERING PHASE WITH "+str(msg.id_src)+" STARTED")
    if msg.id_src in idRegistered:
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot*3))

    if msg.id_src in isRegistered:
        print("Added before")
    else:
        isRegistered.append(msg.id_src)
    #print("REGISTERING PHASE WITH "+str(msg.id_src)+" ENDED")
def standard():
    print("STANDARD PHASE STARTED")
    global isRegistered
    global slot
    data_sum=""
    for idDest in isRegistered:
        print(idDest)
        print('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot*3))
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot*3))

        dataHarvested = s.recv(128)
        msgH =messageLoRa()
        msgH.fillMessage(dataHarvested)
        rnd=Random()
        print("[FIRST Send] for "+str(idDest)+" Request data in "+str(rnd))
        print(dataHarvested)
        time.sleep(rnd)
        while msgH.id_src != str(idDest) or msgH.id_dest != str(id) or msgH.kind != "5" or msgH.messageName != "DataRes":
            rnd=Random()
            print("[Try] for "+str(idDest)+" send Request data in "+str(rnd))
            time.sleep(rnd)
            s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot*3))
            dataHarvested = s.recv(128)
            msgH =messageLoRa()
            msgH.fillMessage(dataHarvested)
            print("msg data =========>"+dataHarvested.decode())
        data_sum=data_sum+str(idDest)+","+str(msgH.data)+":"
    print("STANDARD PHASE ENDED")
    return data_sum
def handle_message(data):
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.kind == "1":
        pairing_phase(msg)
    if msg.kind == "3" and msg.id_dest == str(id):
        registering_phase(msg)
    if msg.kind == "3" and msg.id_dest != str(id):
        if msg.id_src in idRegistered:
            idRegistered.remove(msg.id_src)
            print("Delete ID:"+str(msg.id_src)+"from the table idRegistered")
changetoBluetooth(lora)
time.sleep(2.5)
clock = TimerL(slot,1)
while True:
    if isListening:
        pycom.rgbled(0x007f00) # green
        print("reception ")
        time.sleep(1.500)
        print(" gestion des messages")
        time.sleep(1.500)
        print(" recoltes des datas")
        time.sleep(1.500)
        if recolte !="" :
            changetoA(s,dev_eui,app_key,app_eui,lora)
            print(recolte)
            time.sleep(2)
            send_data(s,recolte)
            changetoBluetooth(bluetooth)
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        del clock
        clock = TimerL(listeningTime,2)
        isListening=True
