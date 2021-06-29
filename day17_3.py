# Task 3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="uday1raj",
    database="pybtcpd17"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Employee1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), city VARCHAR(25))")
sql = "INSERT INTO Employee1 (id, name, city) VALUES (%s, %s, %s)"
val = ("10", "uday", "chirala")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO Employee1 (id, name, city) VALUES (%s, %s, %s)"
val = [
    ("1", "prem", "produtur"),
    ("2", "vamsi", "narsaraopet"),
    ("3", "krishna", "ongole"),
    ("4", "srinadh", "singaraikonda"),
    ("5", "pavan", "ongole")
       ]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "records inserted.")

mycursor.execute("SELECT * FROM Employee1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("SELECT name FROM Employee1")
nameresult = mycursor.fetchall()
for y in nameresult:
    print(y)