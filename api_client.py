"""
	2.	API Client (api_client.py):
	•	Uses the requests library to make GET requests to the weather API.
	•	Handles API authentication using an API key stored in environment variables.
	•	Implements error handling for different HTTP status codes.
"""

import requests


class WeatherApiClient:
    """
    Client for interacting with the OpenWeatherMap API to fetch weather data
    based on latitude and longitude coordinates.
    """

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key) -> None:
        """
        Initializes the API client with the provided API key.

        Args:
            api_key (str): The API key for authenticating with OpenWeatherMap.
        """
        self.api_key = api_key

    def get_weather_data(self, lat: float, lon: float) -> dict:
        """
        Fetches weather data from the OpenWeatherMap API based on the provided
        latitude and longitude.

        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.

        Returns:
            dict: Parsed JSON data containing weather information.

        Raises:
            requests.HTTPError: If the API request returns an error status.
            ValueError: If an invalid API key is used.
        """
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}

        try:
            # Add a timeout to the request
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            return response.json()

        except requests.exceptions.HTTPError as e:
            # Handle HTTP errors
            if response.status_code == 401:
                raise ValueError("Unauthorized: Invalid API key.") from e
            raise
        except requests.exceptions.RequestException as e:
            # Handle other possible request exceptions (timeouts, network issues, etc.)
            raise SystemError("A network error occurred") from e
