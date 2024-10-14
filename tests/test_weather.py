import unittest
from unittest.mock import patch, Mock
import requests
from api_client import WeatherApiClient


class TestWeatherApiClient(unittest.TestCase):
    @patch("api_client.requests.get")
    def test_get_weather_data_success(self, mock_get):
        # Mock a successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "main": {"temp": 15.0, "humidity": 80},
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5.5},
        }
        mock_get.return_value = mock_response

        # Initialize the API client
        api_client = WeatherApiClient("test_api_key")
        result = api_client.get_weather_data(51.5074, -0.1278)

        # Assertions
        self.assertEqual(result["name"], "London")
        self.assertEqual(result["main"]["temp"], 15.0)
        self.assertEqual(result["main"]["humidity"], 80)
        self.assertEqual(result["weather"][0]["description"], "clear sky")
        self.assertEqual(result["wind"]["speed"], 5.5)

    @patch("api_client.requests.get")
    def test_get_weather_data_invalid_api_key(self, mock_get):
        # Mock a 401 Unauthorized response (Invalid API Key)
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        # Initialize the API client
        api_client = WeatherApiClient("invalid_api_key")

        # Expect a ValueError to be raised for invalid API key
        with self.assertRaises(ValueError):
            api_client.get_weather_data(51.5074, -0.1278)

    @patch("api_client.requests.get")
    def test_get_weather_data_network_error(self, mock_get):
        # Simulate a network error (e.g., timeout, connection error)
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        # Initialize the API client
        api_client = WeatherApiClient("test_api_key")

        # Expect a SystemError to be raised for network issues
        with self.assertRaises(SystemError):
            api_client.get_weather_data(51.5074, -0.1278)

    @patch("api_client.requests.get")
    def test_get_weather_data_http_error(self, mock_get):
        # Mock a generic HTTP error (e.g., 404 Not Found)
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        # Initialize the API client
        api_client = WeatherApiClient("test_api_key")

        # Expect an HTTPError to be raised for other non-401 errors
        with self.assertRaises(requests.exceptions.HTTPError):
            api_client.get_weather_data(51.5074, -0.1278)


if __name__ == "__main__":
    unittest.main()
