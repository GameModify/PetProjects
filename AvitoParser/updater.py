from entities import Track
from requests import Session
from parser import AvitoParser
from time import time


class Updater:
    def __init__(self):
        self.__session = Session()

    def create_link(self, track: Track) -> str:
        pass
        return f"https://avito.ru/..../q={track.queue}"

    def update_track(self, track: Track) -> Track:
        print("Обновление трека")
        response = self.__session.get(url=self.create_link(track))
        if response.status_code == 200:
            list_orders = AvitoParser.parse(response.text)
            if list_orders:
                order = list_orders.pop()
                track.last_id = order.id
                # todo check already notif this id
            track.time_last_update = time()
        return track

