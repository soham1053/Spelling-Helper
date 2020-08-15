from source import app
from source.db import query
from flask import render_template, request, session
import bcrypt

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["ps"]
		logged_in = query(f"SELECT * FROM users WHERE username='{username}'")
		if len(logged_in) > 0:
			id, username, hash = logged_in[0]
			if not bcrypt.checkpw(password.encode(), hash.encode()):
				return render_template("login.html")
			else:
				session["logged_in"] = username
				return render_template("home.html")

		return render_template("home.html", logged_in=session["logged_in"], username=username)

	if "logged_in" not in session:
		session["logged_in"] = ""
	return render_template("login.html", logged_in=session["logged_in"], username=session["logged_in"])