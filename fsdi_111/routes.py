#!/usr/bin/env python3
# -*- coding:utf8 -*- 
"""Routes file: Specifies HTTP route"""

from app import appdirs
@app.route("/")
def index():
    return "Hello, World!"
    
@app.route("/about")
def about():
    me = {
        "first_name": "Eric"
        "Last_name": "Babin"
        "hobbies": "Broadcasting"
        "ok": True
        }
    return me
    
