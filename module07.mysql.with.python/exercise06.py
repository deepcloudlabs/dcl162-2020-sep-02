import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

my_cursor = my_connection.cursor()

sql = "update customers set address='istanbul, turkey'"

my_cursor.execute(sql)

my_connection.commit()

print(f"{my_cursor.rowcount} record(s) affected.")