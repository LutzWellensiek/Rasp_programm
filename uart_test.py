import serial
import time

# Öffne serielle Verbindung (z. B. an /dev/serial0)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

# Dauerschleife
while True:
    ser.write(b'Hallo vom Raspberry Pi!\n')
    time.sleep(1)
