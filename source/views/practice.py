from source import app
from flask import render_template, session, redirect, url_for

@app.route("/practice")
def practice():
	if "logged_in" not in session:
		return redirect(url_for("login"))
	elif not session["logged_in"]:
		return redirect(url_for("login"))
	else:
		return render_template("practice.html")
