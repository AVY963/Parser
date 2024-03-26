import pymysql

class Database:
    def __init__(self, host, user, password, dbname):
        self.connection = pymysql.connect(host = host,
                                          port= 6033,
                                          user = user,
                                          password = password,
                                          db = dbname,
                                          charset = 'utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def add_product(self, name, price, id):
        try:
            sql = "INSERT INTO data (name, price, id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE name = VALUES(name), price = VALUES(price)"
            self.cursor.execute(sql, (name, price, id))
            self.connection.commit()

        except pymysql.MySQLError as e:
            print(f"Ошибка при добавлении продукта: {e}")

    def get_data(self, start_index, records_per_page):
        # SQL запрос для извлечения определённого диапазона записей
        query = "SELECT * FROM data LIMIT %s OFFSET %s;"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (records_per_page, start_index))
            data = cursor.fetchall()
        return data

    def get_total_records(self):
        # SQL запрос для получения количества записей в таблице
        query = "SELECT COUNT(*) FROM data;"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            total_records = cursor.fetchone()['COUNT(*)']
        return total_records
