"""
4.	Weather Service (weather_service.py):
	•	Implements business logic for processing and formatting the weather data.
	•	Applies the KISS and SRP principles to separate data fetching, parsing, and displaying.
"""


class WeatherService:
    """
    A service for fetching and processing weather data using an API client.

    This class interacts with the WeatherApiClient to fetch weather information
    and processes the returned data for user-friendly output.
    """

    def __init__(self, api_client) -> None:
        """
        Initializes the WeatherService with the given API client.

        Args:
            api_client: An instance of WeatherApiClient for making API calls.
        """
        self.api_client = api_client

    def get_weather_info(self, lat: float, lon: float) -> dict:
        """
        Fetches weather information for the given latitude and longitude.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.

        Returns:
            dict: A dictionary containing weather information, including place name,
            temperature, humidity, condition, and wind speed.
        """

        data = self.api_client.get_weather_data(lat, lon)
        return {
            "place_name": data["name"],
            "location": f"Lat: {lat}, Lon: {lon}",
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }
