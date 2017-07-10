# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:17:10 2017

@author: Keerthi
"""

from flask import Flask

app = Flask(__name__)

wsgi_app = app.wsgi_app
from routes import *

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    
    try:
        PORT = int(os.environ.get('SERVER_HOST', 'localhost'))
    except ValueError:
        PORT = 5555
    app.run(HOST,PORT)