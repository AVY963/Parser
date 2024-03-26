from config import config
import requests

class WebScraper:
    def __init__(self, db):
        self.db = db

    def get_json_content(self, pstart, pend):
        products = []
        for i in range(int(pstart), int(pend) + 1):
            r = requests.get(config.url.replace("(PAGENUMBER)", str(i))).json()
            for product in r['data']['products']:
                products.append({'name': product['name'], 'price': product['sizes'][0]['price']['total'], 'id': product['id']})
        return products

    def parse(self, pstart, pend):

        data = self.get_json_content(pstart, pend)  # Получение данных с веб-сайта
        # Перебор полученных данных и добавление их в базу данных
        for item in data:  # Предполагаемая структура данных
            name = item['name']
            price = item['price']
            id = item['id']
            self.db.add_product(name, price, id)  # Добавление продукта в базу данных
