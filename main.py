import requests
from twilio.rest import Client
import os

# Authentication info from Twilio:
ACCOUNT_SID = "AC49339c118b248f6c31e783077c669551"
# Environment variable for sensitive data:
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_NUMBER = "+16155812977"

# Open Weather Map API info:
OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# Environment variable for sensitive data:
api_key = os.environ.get("OWM_API_KEY")

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

if will_rain:
    twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = twilio_client.messages \
        .create(
            body="Looks like rain/snow. Bring an umbrella!",
            from_=TWILIO_NUMBER,
            to='+40727718096'
        )
