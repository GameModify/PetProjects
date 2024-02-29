from database import Database
from updater import Updater
from entities import TrackID, Track, TrackList

from time import time, sleep


class AvitoFinder:

    MIN_TIMEOUT_MS = 5

    def __init__(self, db: Database):
        self.db = db
        self.updater = Updater()

    def create_track(self, category, queue, city_id) -> TrackID:
        self.db
        return 1

    def read_track(self, id_: TrackID) -> Track:
        self.db
        return Track()

    def update_track(self, track: Track) -> Track:
        self.db
        return Track()

    def delete_track(self, id_: TrackID) -> bool:
        self.db
        return False

    def get_all_tracks(self) -> TrackList:
        self.db
        return [Track()]

    def clear_all_tracks(self):
        self.db
        pass

    def get_all_need_update_tracks(self) -> TrackList:
        tracks = self.get_all_tracks()
        need_update_tracks: TrackList = []
        for track in tracks:
            if track.time_last_update is None:
                need_update_tracks.append(track)
            elif track.time_last_update + self.MIN_TIMEOUT_MS < time():
                need_update_tracks.append(track)
        return need_update_tracks

    def update(self):
        print("Обновление")
        need_update_tracks = self.get_all_need_update_tracks()
        need_notification_tracks = []
        for track in need_update_tracks:

            updated_track = self.updater.update_track(track)
            if track.last_id is not updated_track.last_id:
                need_notification_tracks.append(track)
            self.update_track(updated_track)
            sleep(self.MIN_TIMEOUT_MS)
        if need_notification_tracks:
            # notification()
            pass

    def start(self):
        start_check = time()
        while True:
            print("Итерация обновления")
            start_check = time()
            self.update()
            delta_time = time() - start_check
            if delta_time < 5:
                sleep(5)





