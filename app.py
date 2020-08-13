from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.cache_control.max = 0
    response.cache_control.public = True 
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/album/<album_id>")
def album(album_id):
    return render_template("album.html",album_id=album_id)

