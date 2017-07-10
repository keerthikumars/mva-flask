# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:17:10 2017

@author: Keerthi
"""

from flask import Flask

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route("/")
def hello():
    "Renders a sample page """
    return "<html><title>KSK</title><h1>KSK</h1></html>"

@app.route("/create")
def create():
    return "<h2> This is simple h2 tag </h2>"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    
    try:
        PORT = int(os.environ.get('SERVER_HOST', 'localhost'))
    except ValueError:
        PORT = 5555
    app.run(HOST,PORT)