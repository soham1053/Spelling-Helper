from source import app
from source.db import query
from flask import render_template, request, session
import bcrypt

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["ps"]

		hashed_pass = password.encode()
		hashed_pass = bcrypt.hashpw(hashed_pass, bcrypt.gensalt(14))		
		query(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_pass.decode('utf-8')}')")
		session["logged_in"] = username
		
		return render_template("home.html")
	elif request.method == "GET":
		return render_template("signup.html")