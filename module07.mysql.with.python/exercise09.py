import mysql.connector

my_connection = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="crmdb")

my_cursor = my_connection.cursor()

sql1 = "insert ...."
sql2 = "update ..."
sql3 = "delete ..."
try: # transaction boundary
    # isolation level: (ansi) read uncommitted, read committed, repeatable read, serializable
    # for long running reporting tasks use "repeatable read" isolation => 'consistent'
    # for web applications/rest api use "read committed" isolation
    my_connection.start_transaction(isolation_level="read committed") # begin
    my_cursor.execute(sql1)
    my_cursor.execute(sql2)
    my_connection.commit() # commit
except:
    my_connection.rollback() # rollback

my_cursor.execute(sql3)
