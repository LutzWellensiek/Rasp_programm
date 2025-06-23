import requests

def get_temperature(city="Berlin", api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    return temp

if __name__ == "__main__":
    # Ersetze 'YOUR_API_KEY' mit deinem OpenWeatherMap API-Schlüssel
    temperature = get_temperature(city="Berlin", api_key="YOUR_API_KEY")
    print(f"Aktuelle Temperatur in Berlin: {temperature}°C")