import os
import requests
import pprint
import json

class DataRequesting(object):
    def __init__(self):
        self.auth = os.environ['weather_auth']
 
    def current_weather(self, city, country_symbol):
        city = str(city.capitalize())
        current_weather = {}
        weather_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}'.format(city) + ',{}'.format(country_symbol) + '&APPID={}'.format(self.auth)).json()
        for weather in weather_request["list"][0:20]:
            current_weather[weather["dt_txt"]] = int(weather["main"]["temp"])-273
        return str(weather_request["country"]) + str(weather_request["city"]) + str(current_weather).replace("{", "").replace("}","")

