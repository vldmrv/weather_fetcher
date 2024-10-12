"""
	1.	Main Script (weather.py):
	•	Entry point for the script.
	•	Accepts user input for the latitude and longitude and displays the weather information.
"""

from weather_service import WeatherService
from api_client import WeatherApiClient
from config import get_api_key


def main():
    """
    Main function to fetch and display weather information for a given latitude and longitude.

    Uses the WeatherApiClient to fetch weather data from the OpenWeatherMap API.
    """
    lat = float(input("Enter the latitude: "))12
    lon = float(input("Enter the longitude: "))
    api_client = WeatherApiClient(get_api_key())
    weather_service = WeatherService(api_client)

    try:
        weather_info = weather_service.get_weather_info(lat, lon)
        print(f"Place Name: {weather_info['place_name']}")
        print(f"Weather in: {weather_info['location']}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Condition: {weather_info['condition']}")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
