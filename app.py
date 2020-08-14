from flask import Flask
from flask import render_template

import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/album/<album_id>")
def album(album_id):
    return render_template("album.html",album_id=album_id)

