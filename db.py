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


    def add_product(self, name, price, id):
        try:
            sql = "INSERT INTO data (name, price, id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE name = VALUES(name), price = VALUES(price)"
            self.cursor.execute(sql, (name, price, id))
            self.connection.commit()

        except pymysql.MySQLError as e:
            print(f"Ошибка при добавлении продукта: {e}")


    def close(self):
        self.connection.close()
