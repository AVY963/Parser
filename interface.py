import streamlit as st
import pandas as pd
import pymysql

# Функция для подключения к базе данных
def connect_to_db():
    return pymysql.connect(
        host='127.0.0.1',
        port=6033,
        user='root',
        password='my_secret_password',
        db='data_parse',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Функция для извлечения данных из базы данных
def get_data(limit):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM data LIMIT {limit}"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Создание интерфейса Streamlit
st.title('Просмотр данных товаров')

# Позволяем пользователю выбрать количество страниц для отображения
pages = st.number_input('Введите количество страниц для отображения:', min_value=1, value=1)
records_per_page = 10  # Количество записей на одной странице
total_records = pages * records_per_page  # Общее количество записей для отображения

data = get_data(total_records)

# Вывод таблицы с данными
df = pd.DataFrame(data)
df.index += 1
# Делаем значения в столбце 'price' на два нуля меньше
df['price'] = df['price'] / 100
df['price'] = df['price'].astype(int)

st.table(df)
