import constants
import requests
import config


def get_weather_info(city: str) -> dict:
    """
    {
      "coord": {
        "lon": 30.7326,
        "lat": 46.4775
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "base": "stations",
      "main": {
        "temp": 17.88,
        "feels_like": 17.86,
        "temp_min": 17.88,
        "temp_max": 17.88,
        "pressure": 1014,
        "humidity": 82,
        "sea_level": 1014,
        "grnd_level": 1011
      },
      "visibility": 10000,
      "wind": {
        "speed": 9.2,
        "deg": 320,
        "gust": 10.03
      },
      "clouds": {
        "all": 75
      },
      "dt": 1781285119,
      "sys": {
        "country": "UA",
        "sunrise": 1781229844,
        "sunset": 1781286591
      },
      "timezone": 10800,
      "id": 698740,
      "name": "Odesa",
      "cod": 200
    }
    """
    params = {
        'appid': config.OPENWEATHERMAP_APPID,
        'q': city,
        'units': 'metric',
    }
    response = requests.get(url=constants.OPEN_WEATHER_API_URL, params=params)
    response_json = response.json()
    result = {
        'temperature': response_json['main']['temp'],
        'wind_speed':  response_json['wind']['speed'],
        'description': response_json['weather'][0]['description']
    }
    return result

