#Weather
import requests

from app.skills.base import Skill

class WeatherSkill(Skill):

    INTENTS = [
        "GET_WEATHER"
    ]
    API_KEY = "9274a692bbf9a3ca3fa94277a1e9ec18"
    url = "https://api.openweathermap.org/data/2.5/weather"

    def handle(self, text: str, intent: str, command: str) -> str:

        city = self.city_search(text)

        if not city:
            return "invalid city"

        params = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric",
            "lang": "ru"
        }
        response = requests.get(self.url, params=params, timeout=10)

        data = response.json()

        if response.status_code != 200:
            return "code 200"

        temp = round(data["main"]["temp"])

        wind_speed = round(data["wind"]["speed"])

        return (
            f"В городе {city} "
            f"сейчас {temp} градусов, "
            f"скорость ветра {wind_speed} км/ч"
        )

    def city_search(self, user_text: str) -> str:
        words = user_text.lower().split()

        if "в" in words:
            index = words.index("в")
            if index + 1 < len(words):
                return words[index + 1]

        if "погода" in words:
            index = words.index("погода")
            if index + 1 < len(words):
                return words[index + 1]

        return ""