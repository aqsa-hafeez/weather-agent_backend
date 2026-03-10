import requests
from langchain.tools import tool
from app.core.config import settings

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    if not city:
        return "Please specify a city."

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": settings.OPENWEATHER_API_KEY, "units": "metric"}

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"Weather in {city.capitalize()}: {temp}°C, {desc.capitalize()}."
    except Exception:
        return f"Error: Unable to retrieve weather for {city}."