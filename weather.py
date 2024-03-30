import requests

key = "7080b85d03b618cd74a84a0fa43249d3"

city = "Пушкино"

def get_weather(key, city):
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
    data = res.json()

    return data