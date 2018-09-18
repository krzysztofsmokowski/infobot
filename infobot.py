import os
import time
import telepot
from datarequesting import DataRequesting

class Infobot(object):
    def __init__(self):
        self.bot = telepot.Bot(os.environ['telepot_auth'])
        self.methods = ["Weather"]
 
    def weather_sender(self, city, country_symbol):
        weather = DataRequesting()
        weather_info = weather.current_weather(city=city, country_symbol=country_symbol)
        try:
            self.bot.sendMessage(os.environ['telepot_id'], weather_info)
        except:
            self.bot.sendMessage(os.environ['telepot_id'], "city not found")

    def message_handler(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        options = "At this moment bot allows you to check weather with command: weather {city} {country or country_symbol}"
        if content_type == 'text':
            self.bot.sendMessage(chat_id, options)
            self.bot.sendMessage(chat_id, 'you asked for : {}'.format(msg['text']))
            if 'weather' or 'Weather' in msg['text']:
                try:
                    splitted_msg = msg['text'].split(' ')
                    self.weather_sender(splitted_msg[1], splitted_msg[2])
                except IndexError:
                    self.bot.sendMessage(chat_id, "unexpected error, not enough arguments".format(msg['text']))

    def test_receiver(self):
        self.bot.message_loop(self.message_handler)


def main():
    info = Infobot()
    info.test_receiver()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()


