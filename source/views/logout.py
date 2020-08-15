from source import app
from flask import render_template, request, session, redirect, url_for


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        session["logged_in"] = ""
        return redirect(url_for("index"))
    else:
        if "logged_in" not in session:
            return redirect(url_for("/login"))
        elif not session["logged_in"]:
            return redirect(url_for("/login"))
        else:
            return render_template("logout.html", username=session["logged_in"])
