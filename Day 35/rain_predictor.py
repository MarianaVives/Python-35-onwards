import requests
from twilio.rest import Client
import os

# --- Twilio ---
account_sid =  os.environ["TWILIO_ACCOUNT_SID"]
auth_token = ""
client = Client(account_sid, auth_token)
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
FROM_NUMBER = "+15017122661"
TO_NUMBER = ""
SMS_BODY = "[RAIN WARNING] Bring an umbrella. Chances of rain are high ☔☔☔."
# --- Weather open map API ---
API_KEY = ""
#set lat and lon to Moscow to test positive scenario: https://www.ventusky.com/moscow shows rain in moscow
LAT = 55.751244
LON = 37.618423

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather",
                            params = parameters)
if print(response.status_code) == 200:
    forecast_data = response.json()
    print(forecast_data)
    weather_id = forecast_data["weather"][0]["id"]
    weather_description = forecast_data["weather"][0]["description"]

    will_rain = False
    if weather_id < 700:
        will_rain = True
        clouds = forecast_data["clouds"]["all"]
        print(f"Carry an umbrella. Current clouds: {clouds}")

    if will_rain:
        print("Bring an umbrella.")
        #Password123.
        message = client.messages.create(
            body=SMS_BODY,
            from_=FROM_NUMBER,
            to= TO_NUMBER,
        )
        print(message.status)