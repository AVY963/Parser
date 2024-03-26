from db import Database
from config import config
import streamlit as st
import pandas as pd

from parser import WebScraper

# Подключения к базе данных
db = Database(config.host, config.user, config.password, config.dbname)
scraper = WebScraper(db)

# Создание интерфейса Streamlit
st.title('Парсинг страниц')
start_number = st.number_input('Начало', value=None, min_value=None, max_value=None, step=1, placeholder="Введите число...", key='start_number')
end_number = st.number_input('Конец', value=None, min_value=None, max_value=None, step=1,  placeholder="Введите число...", key='end_number')
st.button('Спарсить', on_click=lambda: scraper.parse(start_number, end_number))

st.subheader('Просмотр данных товаров')

# Получаем общее количество записей в базе данных
total_records = db.get_total_records()

# Позволяем пользователю выбрать количество страниц для отображения
records_per_page = 100
total_pages = (total_records + records_per_page - 1) // records_per_page

# Выбор страницы пользователем
current_page = st.number_input('Страница', min_value=1, max_value=None, value=1)

# Получаем данные для текущей страницы
start_index = (current_page - 1) * records_per_page
data = db.get_data(start_index, records_per_page)
# Вывод таблицы с данными
if data:
    df = pd.DataFrame(data)
    df.index = pd.RangeIndex(start=start_index + 1, stop=start_index + len(data) + 1, step=1)

    # Делаем значения в столбце 'price' на два нуля меньше и приводим к целому
    df['price'] = (df['price'] / 100).astype(int)

    st.table(df)
else:
    st.write("Нет данных для отображения.")

