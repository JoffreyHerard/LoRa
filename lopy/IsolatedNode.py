from network import LoRa
import socket
import machine
import time
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
while True:
    # send some data
    s.setblocking(True)
    s.send('Discover')
    print("Discover sent")
    # get any data received...
    s.setblocking(False)
    data=s.recv(64)

    print(data)

    # wait a random amount of time
    time.sleep(machine.rng() & 0x0F)
