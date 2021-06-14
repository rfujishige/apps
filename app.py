import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get('http://10.1.10.4/')
    return r.text
