
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


@app.route("/add_user")
def adduser():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
	

if __name__ == "__main__":
	app.run(debug=True, port = 8080, host = '0.0.0.0')