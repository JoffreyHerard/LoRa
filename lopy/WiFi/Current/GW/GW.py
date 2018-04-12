
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
recolte=""
bssid=""
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
        alarm.cancel()
        isListening=True
    def _seconds_handler(self, alarm):
        global isListening
        alarm.cancel()
        isListening=False
def pairing_phase(msg,s):
    global slot
    global idRegistered
    s.sendall('Accept,'+str(2)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot*3)+","+mySSID)
    if msg.id_src in idRegistered:
        print("Added before")
    else:
        idRegistered.append(msg.id_src)
def registering_phase(msg,s):
    global isRegistered
    global slot
    global bssid
    print("Registering phase ")
    s.sendall('DataReq,'+str(4)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(msg.id_src)+','+str(-1)+','+str(slot*3)+","+mySSID)
    if msg.id_src in isRegistered:
        print("Added before")
        print("titi")
    else:
        isRegistered.append(msg.id_src)
def handle_message(data,connection):
    msg =messageLoRa()
    msg.fillMessage(data)
    global recolte
    global nb_harvest
    if msg.kind == "1":
        pairing_phase(msg,connection)
    if msg.kind == "3" and msg.id_dest != str(id):
        registering_phase(msg,connection)
    if msg.kind == "5" and msg.id_dest == str(id):
        recolte=""+msg.id_src+","+msg.data+":"
        nb_harvest=nb_harvest+1

wlan = WLAN()
mySSID="WGW_lopy_"+binascii.hexlify(wlan.mac().decode('utf-8')).decode()
print("My AP name is : "+mySSID)
# configure the WLAN subsystem in station mode (the default is AP)
wlan.init(mode=WLAN.AP, ssid=mySSID,auth=(WLAN.WPA2,'www.python.com'), channel=7, antenna=WLAN.INT_ANT)
#STA config
#wlan.ifconfig(id=0,config=('10.0.0.114', '255.255.0.0', '10.0.0.1', '10.0.0.1'))
#AP config
#wlan.ifconfig(id=1,config=('192.168.4.1', '255.255.255.0', '192.168.4.10', '192.168.0.1'))
print("My ip on the network [AP] is : "+wlan.ifconfig(id=1)[0])
print("My ip on the network [STA] is : "+wlan.ifconfig(id=0)[0])
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.4.1', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
pycom.heartbeat(False)
pycom.rgbled(0x007f00) # green

time.sleep(2.5)
clock = TimerL(slot,1)

while True:
    if isListening:
        pycom.rgbled(0x007f00) # green
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            while isListening:
                data = connection.recv(128)
                print('received {!r}'.format(data))
                if data:
                    handle_message(data,connection)
                    time.sleep(1.500)
                else:
                    print('no data from', client_address)
                    break
        finally:
            connection.close()
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        del clock
        clock = TimerL(listeningTime,2)
        isListening=True
