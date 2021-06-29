# Task 2
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uday1raj',
    database='pybtcpd17'
)

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE IF NOT EXISTS pybtcpd17")

dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)
print("\n")
dbse.execute("CREATE TABLE IF NOT EXISTS table1 (name VARCHAR(20),age INT,gender VARCHAR(10))")
dbse.execute("CREATE TABLE IF NOT EXISTS table2 (fname VARCHAR(20),lname VARCHAR(20),age INT)")
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)


