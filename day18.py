# Day 18
# Task 1
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uday1raj',
    database='pybtcpd17'
)
dbse = mydb.cursor()
dbse.execute(
    "CREATE TABLE IF NOT EXISTS doctorlist (doctorId INT AUTO_INCREMENT PRIMARY KEY, doctorName VARCHAR(20), patientsVisited INT)")

sql = "INSERT INTO doctorlist (doctorId, doctorName, patientsVisited) VALUES (%s, %s, %s)"
val = [('1', 'uday', '10'),
       ('2', 'prem', '5'),
       ('3', 'vamsi', '4'),
       ('4', 'krishna', '0'),
       ('5', 'pavan', '1'),
       ('6', 'srinadh', '0')]

dbse.executemany(sql, val)
mydb.commit()
print(dbse.rowcount, "queries executed")

# Task 2
dbse.execute("SELECT doctorName from doctorlist WHERE patientsVisited > 5")
result = dbse.fetchall()
for x in result:
    print(x)
print("\n")
#Task 3
dbse.execute("SELECT doctorName from doctorlist WHERE patientsVisited = 0")
result1 = dbse.fetchall()
for y in result1:
    print(y)
