import telepot
import os
from datarequesting import DataRequesting
import pprint
import time

class Infobot(object):
    def __init__(self):
        self.bot = telepot.Bot(os.environ['telepot_auth'])
    
    def weather_sender(self, city, country_symbol):
        weather = DataRequesting()
        weather_info = weather.current_weather(city=city, country_symbol=country_symbol)
        self.bot.sendMessage(os.environ['telepot_id'], weather_info)
    
    def _last_message_sent(self):
        response = self.bot.getUpdates()
        return str(response[-1]["message"]["text"]).capitalize()

    def _last_message_utc_time(self):
        response = self.bot.getUpdates()
        return int(response[-1]["message"]["date"])

    def _message_receiver(self):
        if self._last_message_sent() == "Weather" and int(time.time())-(self._last_message_utc_time()) <10:
            self.weather_sender("poznan", "pl")
        

def main():
    info = Infobot()
    while True:
        time.sleep(11)
        info._message_receiver()
if __name__ == '__main__':
    main()


