from project import app
from flask import render_template, redirect, url_for

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')
    