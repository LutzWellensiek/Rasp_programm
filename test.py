import requests
import time

def get_temperature(city="Berlin", api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    return temp

import matplotlib.pyplot as plt

if __name__ == "__main__":
    temperatures = []
    timestamps = []
    api_key = "e23328f8e1c2b12c30a3b13c49c62ddb"
    city = "Pforzheim"

    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot(timestamps, temperatures, marker='o')
    ax.set_xlabel("Zeit (s)")
    ax.set_ylabel("Temperatur (°C)")
    ax.set_title(f"Temperaturverlauf in {city}")

    start_time = time.time()
    for i in range(10):  # 10 Messungen, alle 10 Sekunden
        temp = get_temperature(city=city, api_key=api_key)
        current_time = int(time.time() - start_time)
        temperatures.append(temp)
        timestamps.append(current_time)
        line.set_xdata(timestamps)
        line.set_ydata(temperatures)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.1)
        time.sleep(10)

    plt.ioff()
    plt.show()