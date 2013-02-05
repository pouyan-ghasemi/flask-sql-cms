# This is thje Model for the APP
import os
from hashlib import md5, sha1
import datetime
from flask import Markup
from peewee import *
from werkzeug import secure_filename
from flask_peewee.auth import BaseUser
from app import *

# Tables for the DB
class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    name = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    
    def __unicode__(self):
        return self.username
        
class Note (db.Model):
    title = CharField()
    message = TextField()
    created = DateTimeField(default = datetime.datetime.now)
    
    def __unicode__(self):
        return self.message

        
class Articles (db.Model):
    pageid = IntegerField(unique = True)
    title = CharField(max_lenght = 300)
    webpage = TextField()
    created = DateTimeField(default = datetime.datetime.now)
    iamap =  CharField(max_lenght = 200)
    subsitecode = CharField(max_lenght = 20)
    published = BooleanField()
    def __unicode__(self):
        return self.title
    
class Tag(db.Model):
    
    tag = CharField(max_lenght = 50, primary_key = True, unique = True)
    
    def __unicode__(self):
        return self.tag
    
class Photo(db.Model):
    name = CharField(max_lenght = 40) 
    image = CharField(unique = True)
    
    def __unicode__(self):
        return  self.image

    def save_image(self, file_obj):
        self.image = secure_filename(file_obj.filename)
        full_path = os.path.join(app.config['MEDIA_ROOT'], self.image)
        file_obj.save(full_path)
        self.save()

    def url(self):
        return os.path.join(app.config['MEDIA_URL'], self.image)

    def thumb(self):
        return Markup('<img src="%s" style="height: 80px;" />' % self.url())
    

class PhotoTags(db.Model):
    tags = ForeignKeyField(Tag)
    photo = ForeignKeyField(Photo)
    

