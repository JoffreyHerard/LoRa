from network import LoRa
import socket
import time
import messageLoRa
from messageLoRa import messageLoRa
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
id=2
timer=0
NbIN=0
idRegistered=[]
isRegistered=[]
frequency=1
discovered=False
old_phase=frequency
slot=2
MyLW=0
nb_harvest=0
mycolor="blue"
isListening=True
class TimerL:

    def __init__(self,timing):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, timing, periodic=True)

    def _seconds_handler(self, alarm):
        global isListening
        if isListening:
            isListening=False
def pairing_phase(msg):
    global slot
    global idRegistered
    print("PAIRING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('Accept,'+str(2)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    idRegistered.append(msg.id_src)
    print("PAIRING PHASE WITH "+str(msg.id_src)+" ENDED")
def registering_phase(msg):
    global isRegistered
    global slot
    print("REGISTERING PHASE WITH "+str(msg.id_src)+" STARTED")
    s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    if msg.id_src in isRegistered:
        print("Added before")
    else:
        isRegistered.append(msg.id_src)
    print("REGISTERING PHASE WITH "+str(msg.id_src)+" ENDED")
def ack_data(msg):
    #print("STANDARD PHASE STARTED")
    global slot
    print("I received data : "+str(msg.data))
    s.send('ack,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot))
    #print("STANDARD PHASE ENDED")
def standard():
    print("STANDARD PHASE STARTED")
    global isRegistered
    global slot
    for idDest in isRegistered:
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(idDest)+','+str(-1)+','+str(slot))
        dataHarvested = s.recv(128)
        msgH =messageLoRa()
        msgH.fillMessage(dataHarvested)
        while msgH.id_src != idDest and msgH.id_dest == id and msgH.kind == "5":
            dataHarvested = s.recv(128)
            msgH =messageLoRa()
            msgH.fillMessage(dataHarvested)
    print("STANDARD PHASE ENDED")
def handle_message(data):
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.kind == "1":
        pairing_phase(msg)
    else:
        print("not kind 1")
    if msg.kind == "3" and msg.id_dest == str(id):
        registering_phase(msg)
    else:
        print("not kind 3")
    time.sleep(5)
#TANT QUE PAS JOIN
# create an OTAA authentication parameters
#pp_eui = binascii.unhexlify('70 B3 D5 7E F0 00 49 E1'.replace(' ',''))
#app_key = binascii.unhexlify('7D 10 63 DB 28 2D A8 8E 66 39 7B 70 06 07 1A 6A'.replace(' ',''))
#dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
# join a network using OTAA (Over the Air Activation)
#lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
#while not lora.has_joined():
#    time.sleep(2.5)
#    print('Not yet joined...')

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
#FIN TANT QUE PAS JOIN
clock = TimerL(slot)
while True:
    if isListening:
        data = s.recv(128)
        handle_message(data)
        standard()
    else:
        time.sleep(slot)
        isListening=True
