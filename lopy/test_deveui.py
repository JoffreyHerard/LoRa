from network import LoRa
import binascii

lora = LoRa()
print("DevEUI: %s" % (binascii.hexlify(lora.mac()).decode('ascii')))
