from network import LoRa
import socket
import machine
import time
import messageLoRa
from messageLoRa import messageLoRa
from machine import Timer

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print(lora.frequency())
lora.frequency(868000000)
print(lora.frequency())
