#����������� ����������� ������
import pandas as pd
import sqlalchemy
#������ csv ����
frame = pd.read_csv('C:/Users/23/analyst_test.csv')
#������� ���������� � ����� ������
database_username = 'root'
database_password = ''
database_ip       = 'localhost'
database_name     = 'bookmate'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
#����������� ������ � ��. to_sql ������� �������, � ����� �������, ���� ��� ����������� � ��.
frame.to_sql(con=database_connection, name='users', if_exists='replace')
