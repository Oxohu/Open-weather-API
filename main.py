import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "082e835c163207d90037daf403ca6266"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# User input for city
CITY = input("Enter the city name: ").strip()

# Full request URL
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

# Fetch API respons
response = requests.get(url).json()

# Check if city is found
if response.get("cod") != 200:
    print(f"❌ Could not fetch data for {CITY}. Reason: {response.get('message')}")
else:
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    wind_speed = response['wind']['speed']

    print(f"\n📍 Weather report for {CITY}:")
    print(f"🌡️ Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌥️ General weather: {description.capitalize()}.")
    print(f"🌅 Sunrise at: {sunrise_time.strftime('%H:%M:%S')} AM")
    print(f"🌇 Sunset at: {sunset_time.strftime('%H:%M:%S')} PM")
    print(f"💨 Wind speed: {wind_speed} km/h")
