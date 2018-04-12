import network
import time
import socket
import pycom
# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
print("My ip on the network was BEFORE: "+wlan.ifconfig()[0])
wlan.scan()
toto=wlan.connect('WGW_lopy_240ac4007e70', auth=(network.WLAN.WPA2, 'www.python.com'))

time.sleep_ms(50)
while not wlan.isconnected():
    time.sleep_ms(50)
print("My ip on the network is : "+wlan.ifconfig()[0])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.4.1', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
pycom.heartbeat(False)
pycom.rgbled(0x7f7f00) # yellow
try:
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
