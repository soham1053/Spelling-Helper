from source import app
from flask import render_template, session, redirect, url_for
from fuzzywuzzy import fuzz
import requests
import json

@app.route("/completed/<word>")
def completed(word):
	if "word" not in session:
		return redirect(url_for("login"))

	
	r = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
	out = json.loads(r.text)
	old = session["word"]
	session["word"] = out[0]
        
	return render_template("completed.html", user_word=word, grade=fuzz.ratio(word, old.upper()), word=old.upper())