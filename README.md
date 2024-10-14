# Weather Fetcher

### Description

Weather Fetcher is a simple command-line application that retrieves current weather information for a specified location using the OpenWeatherMap API. The application fetches data such as the current temperature, humidity, wind speed, and weather conditions, based on latitude and longitude.

### Features

- Fetches weather data from the OpenWeatherMap API using latitude and longitude.
- Displays current weather conditions (temperature, humidity, condition, wind speed).
- Implements error handling for invalid API responses or city not found.
- Easy-to-use command-line interface.

### Requirements

- **Python 3.x**
- **Required Libraries**:
  - `requests`

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/vldmrv/weather_fetcher.git
   cd weather_fetcher
   ```

2. **Set Up Virtual Environment** (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory and add your OpenWeatherMap API key.
     ```
     WEATHER_API_KEY=your_openweathermap_api_key
     ```

### Usage

1. **Run the Weather Fetcher**:

   ```bash
   python weather.py
   ```

   - The program will fetch the weather based on pre-defined latitude and longitude values or prompt you for city input in later versions.

2. **Expected Output**:
   ```bash
   Place Name: London
   Weather in: Lat: 51.51, Lon: -0.13
   Temperature: 15°C
   Humidity: 70%
   Condition: clear sky
   Wind Speed: 5.0 m/s
   ```

### Error Handling

- If the API returns a 404 error for invalid coordinates or city, the application will catch the exception and display an appropriate error message.
- Handles network errors and API issues, prompting the user with relevant details.

### Testing

- Unit tests are provided in the `tests/` directory using Python’s `unittest` framework. To run the tests:
  ```bash
  python -m unittest discover tests
  ```

### Future Improvements

- Add support for entering city names and using a geocoding API to convert to lat/lon.
- Provide forecast data for the next 5 days.
- Include more detailed error messages for different status codes.
- Support more weather details (e.g., visibility, pressure, etc.).

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
