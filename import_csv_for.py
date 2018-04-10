# Импортируем необходимые библиотеки
import mysql.connector
import csv

# Создание соединения с нашей базой данных
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'bookmate2'
}
conn = mysql.connector.connect(**config)

# Делаем запросы и получаем результаты
cursor = conn.cursor()

# Создаем таблицу в бд с помощью execute
# Таблица с двумя столбцами user_id и started_at
cursor.execute("CREATE TABLE USERS ( \
                user_id int (10) AUTO_INCREMENT, \
                started_at TIMESTAMP NOT NULL, \
                PRIMARY KEY (user_id)); ")

# Импортируем таблицы в бд

with open('C:/Users/23/analyst_test.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row['user_id'], row['started_at'])
        # Соединение с бд
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'bookmate2'
        }
        conn = mysql.connector.connect(**config)
        sql_statement = "INSERT INTO USERS(user_id , started_at) VALUES (%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement, [(row['user_id'], row['started_at'])])
        conn.commit()

# Не забываем закрыть соединение с базой данных
conn.close()
