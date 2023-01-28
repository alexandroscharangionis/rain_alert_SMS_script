import requests

OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = "64a58c3612db289bb4f64ab7d140d7b9"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat": 44.426765,
    "lon": 26.102537,
    "appid": api_key,
    "exclude": "current,minutely,daily"}
response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
print(weather_data)
