#!/usr/bin/cnv python3
#-*- coding: utf8 -*-
"""Routes file: Specifies HTTP routes"""
from app import app

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/about")
def about():
    me = {
        "first_name": "Eric",
        "last_name": "Babin",
        "hobbies": "Writing",
        "ok" : True,
        }
    return me
    