from flask import Flask, render_templates, redirect, url_for, sessions, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "#QWERTZyol123"
app.pernament_session_lifetime = deltatime(days=10)

db = SQLAlchemy(app)

@app.route("/")
def home():
	return render_templates("index.html")

@app.route("/new_contact")
def new_contact():
	return render_templates("new_contact")

@app.route("/delete_contact")
def delete_account():
	return "OK"

@app.route("/display")
def display():
	return render_templates("display.html")

if __name__ == "__main__":
	db.createall()
	app.run()