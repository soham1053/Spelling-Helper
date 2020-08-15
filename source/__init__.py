# Flask imports
from flask import Flask
app = Flask(__name__)
app.secret_key = "key here"

# Other imports
import source.views
