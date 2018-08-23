import telepot
import os
from datarequesting import DataRequesting
import pprint
import time

class Infobot(object):
    def __init__(self):
        self.bot = telepot.Bot(os.environ['telepot_auth'])
        self.methods = ["Weather"]
    
    def weather_sender(self, city, country_symbol):
        weather = DataRequesting()
        weather_info = weather.current_weather(city=city, country_symbol=country_symbol)
        self.bot.sendMessage(os.environ['telepot_id'], weather_info)
    
    def message_handler(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        if content_type == 'text':
            self.bot.sendMessage(chat_id, 'you asked for : {}'.format(msg['text']))
            if 'weather' in msg['text']:
                splitted_msg = msg['text'].split(' ')
                self.weather_sender(splitted_msg[1], splitted_msg[2])

    def test_receiver(self):
        self.bot.message_loop(self.message_handler)


def main():
    info = Infobot()
    info.test_receiver()
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()


