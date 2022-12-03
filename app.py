
from flask import Flask, redirect, url_for, render_template, request

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello to Yen's Sleeping Tracker Application"


@app.route("/add_user/<user_name>")
def add_user(user_name):
    mycursor.execute("SELECT * FROM Users")
    myresult = mycursor.fetchall()
    if user_name not in myresult:
        sql = "INSERT INTO Users (name, password) VALUES (%s, %s)"
        val = (user_name, "password")
        mycursor.execute(sql, val)
        return redirect(url_for("user_list"))
    else:    
	    return redirect(url_for("user_list"))  


@app.route("/user_list")
def user_list():
    mycursor.execute("SELECT * FROM Users")
    myresult = mycursor.fetchall()
    return myresult 

if __name__ == "__main__":
	app.run(debug=True, port = 8080, host = '0.0.0.0')