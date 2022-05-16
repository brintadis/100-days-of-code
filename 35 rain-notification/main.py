import requests
import os
from twilio.rest import Client

# https://www.twilio.com/try-twilio Twilio Sing Up
# https://home.openweathermap.org/api_keys Your Open Weather Api Keys
# https://www.latlong.net/ To get your latitude and longitude

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = "Your OpenWeather api key"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": "Your latitude (float)",
    "lon": "Your longitude (float)",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='Your Twilio Phone Number',
        to='Receiver phone number'
    )
    print(message.status)
