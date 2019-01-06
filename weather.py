"""
Use Openweather to get weather.

The location can be passed as argument.
"""

import requests
from sys import argv


icon_dict = {
            '01d': '️☀️',
            '01n': '🌑',
            '02d': '🌥️',
            '02n': '🌥️',
            '03d': '☁️',
            '03n': '☁️',
            '04n': '☁️',
            '04d': '☁️',
            '09d': '🌧️',
            '09n': '🌧️',
            '10d': '🌦️',
            '10n': '🌦️',
            '11d': '🌩️',
            '11n': '🌩️',
            '13d': '🌨️',
            '13n': '🌨️',
            '50d': '🌫️',
            '50n': '🌫️'
            }


class OpenWeather():

    def __init__(self, location):
        self.location = location
        self._APPID = 'fd2c04ed7f9802656bd2cc23bddc7ad9'
        self._API_URL = 'http://api.openweathermap.org/data/2.5/weather?{}&appid={}'
        self._LocQuerry = 'q={}'
        self._units = '&units=metric'
        self.WeatherType = ''
        self.Temperature = ''
        self.icon = ''

    def get_weather(self):
        """
        Get the weather of the passed location.
        """
        URL = self._API_URL.format(
                            self._LocQuerry.format(self.location),
                            self._APPID
                            ) + self._units
        response = requests.get(URL).json()
        weather = response['weather']
        main = response['main']
        self.WeatherType = weather[0]['main']
        self.Temperature = main['temp']
        self.icon = icon_dict[weather[0]['icon']]

    def display(self):
        """
        Display the weather in a visually pleasing way.
        """
        print('\n{}  {}, {} °C'.format(
                                    self.icon,
                                    self.WeatherType,
                                    self.Temperature
                                    ))


def main():
    if len(argv) < 2:
        print("Please pass a location name!\a")
        exit(1)
    location = ','.join(argv[1:])
    OpenWeatherObject = OpenWeather(location)
    OpenWeatherObject.get_weather()
    OpenWeatherObject.display()


main()
