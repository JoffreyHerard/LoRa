from network import Bluetooth

import machine
import socket
import pycom
import binascii
import network
from network import WLAN
from machine import RTC

bluetooth = Bluetooth()
bluetooth.set_advertisement(name="lopy1", manufacturer_data="lopy_v1")
bluetooth.start_scan(-1) #Change to 10 to have it searching for 10 sec instead if forever
#bluetooth.stop_scan()
bluetooth.advertise(True)
adv = None
def conn_cb (bt_o):
        events = bt_o.events()
        if  events & Bluetooth.CLIENT_CONNECTED:
            print("Client connected")
        elif events & Bluetooth.CLIENT_DISCONNECTED:
            print("Client disconnected")

        bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

        bluetooth.advertise(True)

        srv1 = bluetooth.service(uuid=b'1234567890123456', isprimary=True)

        chr1 = srv1.characteristic(uuid=b'ab34567890123456', value=5)

        char1_read_counter = 0
        def char1_cb_handler(chr):
            global char1_read_counter
            char1_read_counter += 1
            events = chr.events()
            if  events & Bluetooth.CHAR_WRITE_EVENT:
                print("Write request with value = {}".format(chr.value()))
                print('1')
            else:
                if char1_read_counter < 3:
                    print('Read request on char 1')
                    print('2')
                else:
                    return 'ABC DEF'
                    print('3')

        char1_cb = chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char1_cb_handler)

        srv2 = bluetooth.service(uuid=1234, isprimary=True)

        chr2 = srv2.characteristic(uuid=4567, value=0x1234)
        char2_read_counter = 0xF0
        def char2_cb_handler(chr):
            global char2_read_counter
            char2_read_counter += 1
            if char2_read_counter > 0xF1:
                return char2_read_counter

        char2_cb = chr2.callback(trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
        print('4')

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

while True:
    adv = bluetooth.get_adv()
    if adv and bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'lopy2':

        try:
            bluetooth.connect(adv.mac)

            print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_APPEARANCE))
            print("Connected to device with addr = {}".format(binascii.hexlify(adv.mac)))

            #bluetooth.connect(adv.mac)
            pycom.heartbeat(False)
            for cycles in range(1): # stop after 1 cycles
                pycom.rgbled(0x000080) # blue
                time.sleep(0.5)
                pycom.rgbled(0x000000) # blue
                time.sleep(0.5)
                pycom.rgbled(0x000080) # blue
                time.sleep(0.5)
                pycom.rgbled(0x000000) # blue

            print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_APPEARANCE))

        except:
            #start scanning again
            bluetooth.start_scan(5)

            continue
        break
    else:
        if adv != None:
            print('Hej')
