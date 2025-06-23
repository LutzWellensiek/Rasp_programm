import serial
import time

# Öffne serielle Verbindung auf UART3 (GPIO4/5)
ser = serial.Serial('/dev/ttyAMA3', 115200, timeout=1)

# Dauerschleife
while True:
    message = 'Hallo vom Raspberry Pi!\n'
    print("Sende:", message.strip())
    ser.write(message.encode('utf-8'))
    time.sleep(5)
