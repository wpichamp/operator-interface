from serial import Serial
from time import sleep

port = Serial("COM11", 9600)

count = 0

while True:
    port.write(bytearray([count]))
    count += 1

    print count

    if count > 255:
        count = 0


