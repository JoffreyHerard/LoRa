from network import LoRa
import socket
import time
import pycom
import uos
import binascii
from machine import Timer
data1=0
data2=1
data3=2
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
while(True):
    print("SEND : "+str(data1)+","+str(data2)+","+str(data3))
    s.send(str(data1)+","+str(data2)+","+str(data3))
    print("SLEEP PHASE")
    time.sleep(5)
    data1=data1+1
    data2=data2+1
    data3=data3+1
