from typing import List

TrackID = int

HTML = bytes


class Order:
    id: int


class Track:
    category: int
    city: int
    distance: int
    price: int
    queue: str = ""
    time_last_update: int | None = None
    last_id: int | None = None


TrackList = List[Track]
OrderList = List[Order]
