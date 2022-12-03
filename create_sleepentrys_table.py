import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sleepentry (sleep_id INTEGER,user_id INTEGER, date DATE, sleeptime DATETIME, wakeuptime DATETIME, totalsleep TIME , FOREIGN KEY(user_id) REFERENCES users(user_id) , PRIMARY KEY(sleep_id))")