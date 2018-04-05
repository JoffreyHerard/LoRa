from network import Bluetooth
import binascii
import time
bt = Bluetooth()
bt.set_advertisement(name="lopy2", manufacturer_data="lopy_v2")
# scan until we can connect to any BLE device around
#bt.start_scan(-1)
bt.advertise(True)
while True:
  adv = bt.get_adv()
  if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'lopy1':
      try:
          conn = bt.connect(adv.mac)
          services = conn.services()
          for service in services:
              time.sleep(0.050)
              if type(service.uuid()) == bytes:
                  print('Reading chars from service = {}'.format(service.uuid()))
              else:
                  print('Reading chars from service = %x' % service.uuid())
              chars = service.characteristics()
              for char in chars:
                  if (char.properties() & Bluetooth.PROP_READ):
                      print('char {} value = {}'.format(char.uuid(), char.read()))
                  #if (char.properties() & Bluetooth.PROP_WRITE):
                  characteristic.write("toto")
          conn.disconnect()
          break
      except:
          print("Error while connecting or reading from the BLE device")
          break
  else:
      time.sleep(0.050)
