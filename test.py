import requests
import time
import threading
import serial

def get_temperature(city="Berlin", api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    return temp

import matplotlib.pyplot as plt

if __name__ == "__main__":

    api_key = "e23328f8e1c2b12c30a3b13c49c62ddb"
    city = "Pforzheim"
    stop_flag = False

    def check_input():
        global stop_flag
        while True:
            user_input = input()
            if user_input.strip().lower() == "close":
                stop_flag = True
                break

    input_thread = threading.Thread(target=check_input, daemon=True)
    input_thread.start()

    i = 0
    while not stop_flag:  # Endlosschleife bis "close" eingegeben wird
        temp = get_temperature(city=city, api_key=api_key)
        print(f"Messung {i+1}: Temperatur in {city}: {temp}°C")
        # Öffne die serielle Schnittstelle (UART3: meist /dev/ttyAMA1 oder COMx unter Windows)
        ser = serial.Serial(
            port='COM4',  # Passe dies ggf. an (z.B. '/dev/ttyAMA1' auf Raspberry Pi)
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )

        # Sende die Temperatur als RS485-Signal
        message = f"{temp:.2f}\n"
        ser.write(message.encode('utf-8'))
        ser.flush()
        for _ in range(100):  # 10 Sekunden in 0.1s-Schritten, damit schneller auf "close" reagiert wird
            if stop_flag:
                break
            time.sleep(0.1)
        i += 1

    print("Messungen beendet.")
