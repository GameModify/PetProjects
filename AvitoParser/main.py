from avito_finder import AvitoFinder
from database import Database


def main():
    db = Database("/")
    # if db.connect():
    if True:
        finder = AvitoFinder(db=db)
        finder.start()
    else:
        print("Ошибка подключения к бд")


if __name__ == '__main__':
    main()
