from entities import Order, OrderList


class AvitoParser:

    @staticmethod
    def parse(body: str) -> OrderList:

        return [Order()]
