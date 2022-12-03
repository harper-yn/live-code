import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE Users (
    user_id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    password varchar(255),
    PRIMARY KEY (user_id)
)
""")