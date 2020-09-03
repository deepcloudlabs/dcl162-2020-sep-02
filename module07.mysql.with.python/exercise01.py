import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

print(my_connection.sql_mode)

my_cursor = my_connection.cursor()

# my_cursor.execute("show databases")

my_cursor.execute("show tables")

for tbl in my_cursor:
    print(tbl[0])