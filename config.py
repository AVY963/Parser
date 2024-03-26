
class Config:
    # URL веб-сайта для парсинга
    url = 'https://catalog.wb.ru/catalog/men_clothes3/v2/catalog?appType=1&cat=129176&curr=rub&dest=-1257786&page=(PAGENUMBER)&sort=popular&spp=30'

    # Данные для подключения к базе данных
    host = '127.0.0.1'
    user = 'root'
    password = 'my_secret_password'
    dbname = 'data_parse'
config = Config()