
import socket
import time
import pycom
import uos
import binascii
import struct
import machine
import sys
import network
from network import LoRa
from network import WLAN
from machine import Timer
from messageLoRa import messageLoRa
wlan = WLAN()
mySSID="WGW_lopy_"+binascii.hexlify(wlan.mac().decode('utf-8')).decode()
print("My AP name is : "+mySSID)
# configure the WLAN subsystem in station mode (the default is AP)
wlan.init(mode=WLAN.STA_AP, ssid=mySSID,auth=(WLAN.WPA2,'www.python.com'), channel=7, antenna=WLAN.INT_ANT)
#STA config
#wlan.ifconfig(id=0,config='dhcp')
#AP config
#wlan.ifconfig(id=1,config="dhcp")
print("My ip on the network [AP] is : "+wlan.ifconfig(id=1)[0])
print("My ip on the network [STA] is : "+wlan.ifconfig(id=0)[0])
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.4.1', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
pycom.heartbeat(False)
pycom.rgbled(0x007f00) # green
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
