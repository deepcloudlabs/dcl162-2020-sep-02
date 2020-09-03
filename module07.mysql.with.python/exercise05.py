import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

my_cursor = my_connection.cursor()

#sql = "select * from customers limit 100,25"
sql = "select * from customers limit 25 offset 100"

my_cursor.execute(sql)

result_set = my_cursor.fetchall()

for row in result_set:
    print(row)
