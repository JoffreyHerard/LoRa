from network import LoRa
import socket
import machine
import uos
import time
import pycom
import network
import binascii
from network import WLAN
import re
from messageLoRa import messageLoRa
from machine import Timer

pycom.heartbeat(False)
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
def notDiscovered(wlan,nameAP):
    global tryDiscover
    global discovered
    global id
    global frequency
    global slot
    wlan.connect(nameAP, auth=(network.WLAN.WPA2, 'www.python.com'))
    time.sleep_ms(50)
    while not wlan.isconnected():
        time.sleep_ms(50)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data=None
    # Connect the socket to the port where the server is listening
    server_address = ('192.168.4.1', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    sock.settimeout(slot)
    pycom.heartbeat(False)
    pycom.rgbled(0x3333ff) # blue
    try:
        payload='Discover,'+str(1)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(-1)+','+str(-1)+','+str(-1)+','+mySSID
        message=payload.encode('utf-8')
        print('sending {!r}'.format(message))
        sock.sendall(message)
        data = sock.recv(128)
        print('received {!r}'.format(data))
    except OSError as err:
        print("OS error: {0}".format(err))
    #finally:
    #    print('closing socket')
    #    sock.close()
    msg =messageLoRa()
    msg.fillMessage(data)
    if msg.messageName == "Accept":
        discovered=True
        myAP=nameAP
        print("I am Discovered")
        pycom.rgbled(0x007f00) # green
        return True
    else:
        pycom.rgbled(0x007f00) # green
        return False

def notRegistered():
      global registered
      global myLoRa
      global tryRegister
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      data=None
      server_address = ('192.168.4.1', 10000)
      print('connecting to {} port {}'.format(*server_address))
      sock.settimeout(slot)
      try:
          sock.connect(server_address)
      except OSError as err:
          print("OS error: {0}".format(err))
      except EAGAIN as err:
          print("EAGAIN error: {0}".format(err))
      pycom.heartbeat(False)
      pycom.rgbled(0x3333ff) # blue
      try:
          payload='Register,'+str(3)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(-1)+','+str(-1)+','+mySSID
          message=payload.encode('utf-8')
          print('sending {!r}'.format(message))
          sock.sendall(message)
          data = sock.recv(128)
          print('received {!r}'.format(data))
      except OSError as err:
          print("OS error: {0}".format(err))
      finally:
          print('closing socket')
          sock.close()
      msg =messageLoRa()

      if data !=None :
          msg.fillMessage(data)
      if msg.messageName == "DataReq":
          registered=True
          print("I am registered")
      else:
          tryRegister+=1
          print("I am NOOOOOT registered"+msg.messageName)
          print(data)
          time.sleep(5)
      pycom.rgbled(0x007f00) # green

def sendData(connection):
    #send some data
    global tryDataReq
    global data
    global myLoRa
    global id
    global slot
    global frequency
    pycom.heartbeat(False)
    pycom.rgbled(0x3333ff) # blue
    try:
        payload='DataRes,'+str(5)+','+str(frequency)+','+str(slot)+','+str(id)+','+str(myLoRa)+','+str(data)+','+str(70)+','+mySSID
        message=payload.encode('utf-8')
        print('sending {!r}'.format(message))
        connection.sendall(message)
    finally:
        print('closing socket')
        connection.close()
    pycom.rgbled(0x007f00) # green
    print("DataResponse sent")

mySSID=""
id=1
timer=0
data=42
tryDiscover=0
tryRegister=0
discovered=False
registered=False
ack_Data=False
frequency=1.0
old_phase=frequency
slot=10
myLoRa=-1
tryDataReq=-1
isListening=True
clock=None
listeningTime=10.0
myAP=None
wlan = network.WLAN()
mySSID="IN_W_"+binascii.hexlify(wlan.mac().decode('utf-8')).decode()
print("My AP name is : "+mySSID)
wlan.init(mode=WLAN.STA)
print("My ip on the network [AP] is : "+wlan.ifconfig(id=1)[0])
print("My ip on the network [STA] is : "+wlan.ifconfig(id=0)[0])
pycom.rgbled(0x007f00) # green
nets = wlan.scan()
while not discovered :
    for networkTarget in nets:
        if re.search("^(WGW_lopy_)",networkTarget.ssid)!=None and not discovered:
            print ("current SSID is : "+networkTarget.ssid)
            notDiscovered(wlan,networkTarget.ssid)
while not registered and discovered:
    notRegistered()
wlan.disconnect()
wlan.deinit()
wlan.init(mode=WLAN.AP, ssid=mySSID,auth=(WLAN.WPA2,'www.python.com'), channel=7, antenna=WLAN.INT_ANT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.4.1', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    if isListening:
        pycom.heartbeat(False)
        pycom.rgbled(0x7f7f00) # yellow
        sock.settimeout(slot)
        print('waiting for a connection from gateway')
        connection=None
        client_address=None
        try:
            connection, client_address = sock.accept()
            print('connection from', client_address)
            dataR = connection.recv(128)
            print('received {!r}'.format(data))
            if dataR:
                msg =messageLoRa()
                msg.fillMessage(dataR)
                if msg.kind=="4" and msg.bssid == mySSID:
                    sendData(connection)
                    print("I sent my data")
                    print("I try to change my slot and listening time")
                    slot=float(msg.slots)
                    sock.settimeout(slot)
                    listeningTime=float(msg.listeningtime) #slot d'une duree de 40 seconde
                    isListening=False
                    del clock
                    clock = TimerL(slot,0)
                time.sleep(1.500)
            else:
                print('no data Request from', client_address)
                break
        except OSError as err:
            print("OS error: {0}".format(err))
            if connection !=None:
                connection.close()
        except EAGAIN as err:
            print("EAGAIN error: {0}".format(err))
            if connection !=None:
                connection.close()
        finally:
            if connection !=None:
                connection.close()

        pycom.rgbled(0x007f00) # green
    else:
        pycom.rgbled(0x7f0000) #red
        print("I am sleeping")
        time.sleep(slot)
        del clock
        clock = TimerL(listeningTime,0)
        isListening=True
