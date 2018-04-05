from network import LoRa
import socket
import time
import binascii
import struct
def changetoLW():
    global app_eui
    global app_key
    global dev_eui
    global lora
    global s
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui, app_key), timeout=0)
    while not lora.has_joined():
        time.sleep(2.5)
        print('CtLW : Not yet joined...')
    print('Connected to Objenious LoRaWAN again !')
def changetoLoRa(lora):
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
    print('Radio mode is LoRa now !')
    time.sleep(5)
def send_datatoLWGW(socket,dataString):
    print("Send data to the LWGW")
    data=dataString
    taille=str(len(data))+'s'
    databytes = struct.pack(taille, data)
    socket.send(databytes)

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
app_eui = binascii.unhexlify('70 B3 D5 7E F0 00 49 E1'.replace(' ',''))
app_key = binascii.unhexlify('30 4C 99 26 3E A5 E6 43 B5 A0 8C B3 25 4A 61 FA'.replace(' ',''))
dev_eui = binascii.unhexlify((binascii.hexlify(lora.mac()).decode('ascii')).upper())
#dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print('connected to Objenious LoRaWAN!')
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)
changetoLoRa(lora)
changetoLW()
send_datatoLWGW(s,"toto,23:")
changetoLoRa(lora)
s.setblocking(False)
