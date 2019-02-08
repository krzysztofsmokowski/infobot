import requests
from bs4 import BeautifulSoup

class AirPollution(object):
    def __init__(self):
        self.all_stations = requests.get("http://api.gios.gov.pl/pjp-api/rest/station/findAll").json()

    def station_dict(self):
        dict_of_stations = {}
        for station in self.all_stations:
            dict_of_stations[station["id"]] = station["stationName"]
        return dict_of_stations

    def station_info(self, city):
        dicto = self.station_dict()
        requested_data = 0
        for key, station in dicto.items():
            if city in station:
                requested_data = requests.get("http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{}".format(key)).text
                '''todo: iterate over http://api.gios.gov.pl/pjp-api/rest/station/sensors/{stationId} in order to get sensor id?'''
        return requested_data

'''
def main():
    air = AirPollution()
    print(air.station_info("Wrocław"))

if __name__ == "__main__":
    main()
'''
