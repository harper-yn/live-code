import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (user_id INTEGER, name VARCHAR(255), password VARCHAR(255), PRIMARY KEY(user_id))")