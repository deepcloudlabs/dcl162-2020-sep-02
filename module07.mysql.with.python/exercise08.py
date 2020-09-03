import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

my_cursor = my_connection.cursor()

sql = "select ctry.name, city.name from country as ctry inner join city as city on ctry.capital = city.id limit 10"

my_cursor.execute(sql)

result_set = my_cursor.fetchall()

for row in result_set:
    print(row)


