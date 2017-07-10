# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:23:23 2017

@author: Keerthi
"""
from flask import Flask, url_for
from app import app

@app.route("/")
def hello():
    createLink = "<a href='" + url_for('create') + "'>Create A Question </a>"
    "Renders a sample page """
    return """
            <html>
              <head> 
                  <title>Welcome KSK!</title>
              </head>
              <body><h1>KSK</h1><p>"""+ createLink + """</body></html>"""


@app.route("/create")
def create():
    return "<h2> This is simple h2 tag for Create Page </h2>"

@app.route("/question/<title>")
def question(title):
    return "<h2>" + title + "</h2>"

