"""
	3.	Configuration (config.py):
	•	Reads the API key from an environment variable and provides a configuration interface for the application.
"""

import os


def get_api_key():
    """
    Retrieves the API key from the environment variable WEATHER_API_KEY.

    Returns:
        str: The API key if it exists, None otherwise.
    """
    return os.getenv("WEATHER_API_KEY")


# Check if the API key is available, and raise an error if it's not set
if not get_api_key():
    raise EnvironmentError("Please set the WEATHER_API_KEY environement variable.")
