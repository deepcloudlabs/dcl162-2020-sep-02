import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

my_cursor = my_connection.cursor()

my_cursor.execute("create table customers ("
                  "id int auto_increment primary key, "
                  "name varchar(255), "
                  "address varchar(255))"
                  )
