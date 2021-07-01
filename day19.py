import xlrd
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='uday1raj',
    database='pybtcpd17'
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE IF NOT EXISTS studentslist (rollno INT PRIMARY KEY, name VARCHAR(25), year INT, "
             "branch VARCHAR(5),percentage FLOAT)")

loc = ("D:\\work\\python 30 days boot camp\\day19_excel.xlsx")
l = list()
a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0, 0)
for i in range(1, 8):
    l.append(tuple(sheet.row_values(i)))

q = "INSERT INTO studentslist (rollno, name, year, branch, percentage) VALUES (%s,%s,%s,%s,%s)"
dbse.executemany(q, l)
mydb.commit()
mydb.close()