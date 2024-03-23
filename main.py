from parser import WebScraper
from db import Database

def main():
    # URL веб-сайта для парсинга
    url = 'https://catalog.wb.ru/catalog/men_clothes3/v2/catalog?appType=1&cat=129176&curr=rub&dest=-1257786&page=(PAGENUMBER)&sort=popular&spp=30'

    # Данные для подключения к базе данных
    host = '127.0.0.1'
    user = 'root'
    password = 'my_secret_password'
    dbname = 'data_parse'

    # Создание объекта для парсинга веб-сайта
    scraper = WebScraper(url)
    data = scraper.get_json_content(20)  # Получение данных с веб-сайта

    # Создание объекта для работы с базой данных
    db = Database(host, user, password, dbname)

    # Перебор полученных данных и добавление их в базу данных
    for item in data:  # Предполагаемая структура данных
        name = item['name']
        price = item['price']
        id = item['id']
        db.add_product(name, price, id)  # Добавление продукта в базу данных

if __name__ == '__main__':
    main()
