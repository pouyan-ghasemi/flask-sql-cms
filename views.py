# views.py
import datetime
from time import time
from flask import request, redirect, url_for, render_template, flash

from flask_peewee.utils import get_object_or_404, object_list
from flask import Markup
from app import app
from auth import auth
from models import User, Note, Tag, Photo, PhotoTags, Articles

from flask.ext.wtf import (Form, TextField, TextAreaField, PasswordField, 
                           SubmitField, Required, ValidationError)


@app.route('/')
def index():
	return get_ia_content("Programs")
	
	
@app.route('/map/<iamap>')	
def get_ia_content(iamap):
	ia = Articles.select().group_by(Articles.iamap);
	content = Articles.select().where(Articles.iamap == iamap )
	return render_template('maps.html', content = content, ia = ia)
	
	
@app.route('/page/<int:pageid>')	
def get_page_content(pageid):
	ia = Articles.select().group_by(Articles.iamap);
	content = Articles.select().where(Articles.pageid == pageid ).limit(1)
	t0 = time()
	value = content[0]
	value.webpage = Markup(value.webpage)
	t1 = time()
	print 'Query from Articles takes %f' %(t1-t0)
	return render_template('page.html', content = value , ia = ia)	
	
	
	