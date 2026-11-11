import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    print("Error: API key not found. Check your .env file.")
    exit()
    
city = input("Enter city name: ").strip()

if not city:
    print("Error: City name cannot be empty.")
    exit()
    
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(URL, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    print("\n--- Weather Report ---")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect. Check your internet connection.")

except requests.exceptions.HTTPError as error:

    status_code = error.response.status_code

    if status_code == 401:
        print("Error: Invalid API key.")

    elif status_code == 404:
        print("Error: City not found.")

    elif status_code == 429:
        print("Error: API rate limit exceeded.")

    elif 500 <= status_code <= 599:
        print("Error: Weather service is experiencing server problems.")

    else:
        print(f"HTTP Error: {status_code}")
        
except requests.exceptions.RequestException:
    print("Error: An unexpected request error occurred.")

