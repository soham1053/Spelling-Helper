from source import app
from flask import render_template, session, redirect, url_for
import json
import requests


@app.route("/practice")
def practice():
    if "logged_in" not in session:
        return redirect(url_for("login"))
    elif not session["logged_in"]:
        return redirect(url_for("login"))
    else:
        r = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
        out = json.loads(r.text)
        if "word" not in session:
            session["word"] = out[0]
        
        return render_template("practice.html", word=session["word"])
