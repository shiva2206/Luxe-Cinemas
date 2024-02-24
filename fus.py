import pandas
import mysql.connector as mq
mydb  = mq.connect(
    host = "localhost",
    user = "root",
    password = "#Mysql123",
    database = "school"
    )
cursor = mydb.cursor()
df = pandas.read_csv("login details.csv")

for k ,v in df.iterrows():
    cursor.execute('INSERT INTO pullingo VALUES'+str(tuple(v)))
    print(str(tuple(v)))
    mydb.commit()
    
