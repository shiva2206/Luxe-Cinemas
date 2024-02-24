import mysql.connector as mc
import pandas as pd
mydb=mc.connect(
	host='localhost',
	database='school',
	user='root',
	password='#Mysql123'
	)
cursor=mydb.cursor()

cursor.execute("SELECT * FROM employee")
record=cursor.fetchall()
empdf=pd.DataFrame(record,dtype=int,columns=cursor.column_names)
print(empdf)
