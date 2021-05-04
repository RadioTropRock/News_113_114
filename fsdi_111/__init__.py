#!/usr/bin/env python3
# =*= coding: utf8 -*-
"""Database models"""

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.first_name


#below is example

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is: %s<p>" % user_agent

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)
