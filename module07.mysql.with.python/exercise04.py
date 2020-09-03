import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

my_cursor = my_connection.cursor()

sql = "insert into customers(name, address) values (%s,%s)"

"""
values = [("james sawyer", "ankara, turkey"), ("jin kwon", "izmir, turkey")]
my_cursor.executemany(sql,values) # bulk insert
my_connection.commit()
"""
"""
for val in values:
    my_cursor.execute(sql,val)
    my_connection.commit()
    print(f"{my_cursor.rowcount} records inserted.")
"""
my_cursor.execute(sql, ("jack bauer", "eskisehir, turkey"))
my_connection.commit()
print(f"id is {my_cursor.lastrowid}.")
print(f"{my_cursor.rowcount} records inserted.")

