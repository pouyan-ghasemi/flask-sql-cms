# app.py
from flask import Flask

from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    User.create_table()
    Tag.create_table()
    Photo.create_table()
    PhotoTags.create_table()
    Note.create_table()
    Articles.create_table()