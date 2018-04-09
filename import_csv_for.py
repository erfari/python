# ����������� ����������� ����������
import pandas as pd
import sqlalchemy
import mysql.connector
import csv

# �������� ���������� � ����� ����� ������
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'bookmate2'
}
conn = mysql.connector.connect(**config)

#������ ������� � �������� ����������
cursor = conn.cursor()

#������� ������� � �� � ������� execute
#������� � ����� ��������� user_id � started_at 
cursor.execute("CREATE TABLE USERS ( \
                user_id int (10) AUTO_INCREMENT, \
                started_at TIMESTAMP NOT NULL, \
                PRIMARY KEY (user_id)); ")

#����������� ������� � ��

with open('C:/Users/23/analyst_test.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['user_id'], row['started_at'])
#���������� � ��
        config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'bookmate2'
                }
        conn = mysql.connector.connect(**config)
        sql_statement = "INSERT INTO USERS(user_id , started_at) VALUES (%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['user_id'], row['started_at'])])
        conn.commit()
        

# �� �������� ������� ���������� � ����� ������
conn.close()
