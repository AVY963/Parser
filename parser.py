import requests

class WebScraper:
    def __init__(self, url):
        self.url = url


    def get_json_content(self, pnum):
        products = []
        for i in range(1, pnum + 1):
            r = requests.get(self.url.replace("(PAGENUMBER)", str(i))).json()

            for product in r['data']['products']:
                products.append({'name': product['name'], 'price': product['sizes'][0]['price']['total'], 'id': product['id']})
        return products
