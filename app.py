from flask import Flask
from flask import render_template
import boto3

import os

from config import S3_BUCKET, S3_KEY, S3_SECRET
from utils import albums

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html", albums=albums)

@app.route("/album/<album_title>")
def album(album_title):
    for album in albums:
        if album.title == album_title:
            images = album.images

    return render_template("album.html",album_title=album_title,images=images)

