# Day20
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uday1raj',
    database='pybtcpd17'
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE IF NOT EXISTS Employee (empId INT, empName VARCHAR(20), salary FLOAT)")
'''sql = 'INSERT INTO Employee (empId, empName, salary) VALUES(%s,%s,%s)'
val = [
    ('1', 'uday', '40000'),
    ('2', 'prem', '35000'),
    ('3', 'vamsi', '40000'),
    ('4', 'krishna', '38000'),
    ('5', 'pavan', '35000'),
    ('6', 'krishnappa', '25000'),
    ('7', 'krithika', '37000')
]
dbse.executemany(sql, val)
mydb.commit()
print(dbse.rowcount, "rows were inserted.")'''

# Task1
dbse.execute("SELECT empName,salary FROM Employee where salary = (select max(salary) from Employee)")
result1 = dbse.fetchall()
for i in result1:
    print(i)
print('\n')
dbse.execute("SELECT empName,salary FROM Employee where salary = (select min(salary) from Employee)")
result2 = dbse.fetchall()
for j in result2:
    print(j)
print('\n')

# Task 2
dbse.execute("SELECT COUNT(*) FROM Employee")
result3 = dbse.fetchall()
for x in result3:
    print(x)
print('\n')

# Task3
dbse.execute("SELECT empName FROM Employee WHERE empName LIKE('kri%')")
result4 = dbse.fetchall()
for y in result4:
    print(y)
