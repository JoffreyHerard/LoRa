
#-- lora1.py, test of objenious uplink / downlink
# by raxy asOf 20jun17 : works OK in class C!
from network import LoRa
import socket
import time
import binascii
import struct

def lora_cb(lora):
    global s
    events = lora.events()
    if events & LoRa.RX_PACKET_EVENT:
        data = s.recv(64) # will return immediately w/ or w/o data
        print("<<",data)

# create an OTAA authentication parameters
app_eui = binascii.unhexlify('70 B3 D5 7E F0 00 49 E1'.replace(' ',''))

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, adr=True, device_class=LoRa.CLASS_A)
#your Class A keys
dev_eui = binascii.unhexlify('70B3D5499C3DD0AC')
app_key = binascii.unhexlify('zzz'.replace(' ','')) #classe A

# xor Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, device_class=LoRa.CLASS_C, adr=True)
#your Class C keys
dev_eui = binascii.unhexlify('xxx') #classe C
app_key = binascii.unhexlify('yyy') #classe C

print('dev_eui==',dev_eui)

# join a network using OTAA (mandatory on objenious WAN)
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    print('joining..')
    time.sleep(3.0)
print('connected to Objenious LoRaWAN!')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
lora.callback(trigger=(LoRa.RX_PACKET_EVENT), handler=lora_cb)

# loop for class C
# make socket non-blocking
s.setblocking(False)
print('waiting...')
while True:
    time.sleep(1.5)
