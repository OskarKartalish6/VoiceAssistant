#Weather
import requests

API_KEY = "9274a692bbf9a3ca3fa94277a1e9ec18"
CITY = "Hamburg"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric",   #°C
    "lang": "ru"
}

response = requests.get(url, params=params)
data = response.json()

print(data)