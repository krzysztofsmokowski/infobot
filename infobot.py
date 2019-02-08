import os
import time
import telepot
from datarequesting import DataRequesting

class Infobot(object):
    def __init__(self):
        self.bot = telepot.Bot(os.environ['telepot_auth'])
        self.options = "At this moment bot allows you to check weather with command: weather {city} {country or country_symbol}"

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
        if content_type == 'text':
            self.bot.sendMessage(chat_id, 'you asked for : {}'.format(msg['text']))
            if 'weather' in msg['text'] or "Weather" in msg['text']:
                try:
                    splitted_msg = msg['text'].split(' ')
                    self.weather_sender(splitted_msg[1], splitted_msg[2])
                except IndexError:
                    self.bot.sendMessage(chat_id, "unexpected error, not enough arguments".format(msg['text']))
            if "air" in msg['text'] or "Air" in msg['text']:
                try:
            else:
                self.bot.sendMessage(chat_id, "wrong command")

    def help(self, msg):
        content_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            if "options" in msg['text']:
                self.bot.sendMessage(chat_id, self.options)

    def test_receiver(self):
        self.bot.message_loop(self.message_handler)

def main():
    info = Infobot()
    info.test_receiver()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()


