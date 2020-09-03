import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123")

my_cursor = my_connection.cursor()

my_cursor.execute("create database crmdb")