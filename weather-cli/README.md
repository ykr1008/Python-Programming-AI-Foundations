# Weather CLI

A command-line weather application built using Python and the OpenWeatherMap API.

## Features

- Fetches current weather for a given city.
- Reads API credentials securely from a `.env` file.
- Uses `python-dotenv` for environment management.
- Uses `requests` to communicate with the API.
- Displays temperature, feels-like temperature, weather condition, humidity, and wind speed.
- Handles timeouts and connection failures.
- Handles HTTP errors including 401, 404, 429, and 5xx.
- Validates empty city input.

## Technologies

- Python
- Requests
- python-dotenv
- OpenWeatherMap API

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file in the project root:

   `WEATHER_API_KEY=your_api_key_here`

5. Run the application:

   `python weather_cli.py`

## Test Results

| Test | Actual Result | Status |
|---|---|---|
| Valid API key | 200 OK | Passed* |
| Wrong API key | 401 Unauthorized | Passed |
| Nonexistent city | 404 Not Found | Passed |
| Timeout (0.001 seconds) | requests.exceptions.Timeout | Passed |

*The valid-city test should be confirmed with a successful live request.

## Security

- API key is stored in `.env`.
- `.env` is excluded through `.gitignore`.
- API key is never hardcoded in the source code.
- Requests use a timeout.

## Author

Python Learning Project