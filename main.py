from serial import Serial
from time import sleep

port = Serial("COM11", 9600)

count = 0

while True:

    tx = [count]

    port.write(bytearray(tx))

    rx = ord(port.read(1))

    print "RX: " + str(rx) + " TX: " + str(tx)

    count += 1

    if count > 255:
        count = 0


