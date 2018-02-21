from network import LoRa
import socket
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

id=2
timer=0
NbIN=0
idRegistered=[]
isRegistered=[]
frequency=1
discovered
old_phase=frequency
slot=5
MyLW=0
nb_harvest=0
mycolor="blue"

def pairing_phase(msg):
        s.send('Accept,'+str(2)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1))
        idRegistered.append(msg.id_src)
def registering_phase(msg):
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1))
        isRegistered.append(msg.id_src)
def standard():
    for id in isRegistered
        s.send('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(id)+','+str(-1))

def handle_message(data):
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.kind == 1:
        pairing_phase(msg)
    if msg.kind == 3:
        registering_phase(msg)





#TANT QUE PAS JOIN
# create an OTAA authentication parameters
app_eui = binascii.unhexlify('70 B3 D5 7E F0 00 49 E1'.replace(' ',''))
app_key = binascii.unhexlify('7D 10 63 DB 28 2D A8 8E 66 39 7B 70 06 07 1A 6A'.replace(' ',''))
#dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
#FIN TANT QUE PAS JOIN
while True:
    data = s.recv(128)
    handle_message(data)
    def standard()
    time.sleep(slots)
