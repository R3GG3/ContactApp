from flask import Flask, render_template, redirect, url_for, sessions, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "#QWERTZyol123"
app.pernament_session_lifetime = timedelta(days=10)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///contacts.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class contacts(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column("name", db.String(100))
	email = db.Column("email", db.String(100))
	number = db.Column("number", db.Integer)

	def __init__(self, name, email, number):
		self.name = name
		self.email = email
		self.number = number

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/new_contact", methods=["POST", "GET"])
def new_contact():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		number = request.form["number"]
		try:
			x = int(number)
			number = x
			del x
		except:
			flash("Wrong Phone Number!")
			return render_template("new_contact.html")

		filter_name = contacts.query.filter_by(name=name).first()
		if filter_name:
			flash("This contact is already registered!")
		else:
			nm = contacts(name, email, number)
			db.session.add(nm)
			db.session.commit()
			flash("Succesfully added new contact!")

	return render_template("new_contact.html")

@app.route("/delete", methods=["POST", "GET"])
def delete_account():
	if request.method == "POST":
		number = request.form["number"]
		contacts.query.filter_by(number=number).delete()
		db.session.commit()
		flash("Contact Deleted Succesfully!")
		return redirect(url_for("home"))
	else:
		return render_template("delete.html")

@app.route("/display")
def display():
	return render_template("display.html", display=contacts.query.all())

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)