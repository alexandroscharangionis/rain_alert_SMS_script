import requests
from twilio.rest import Client

# Authentication info from Twilio:
ACCOUNT_SID = "AC49339c118b248f6c31e783077c669551"
AUTH_TOKEN = "ca62675bb82f970e875baec4373df27f"

# Open Weather Map API info:
OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat": 44.426765,
    "lon": 26.102537,
    "appid": api_key,
    "exclude": "current,minutely,daily"}
response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_data_12_hours = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_data_12_hours:
    weather_condition_code = hour_data["weather"][0]["id"]
    if int(weather_condition_code) < 700:
        will_rain = True
