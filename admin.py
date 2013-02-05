# this is a the admin for the app
import datetime
from flask import request, redirect
from flask_peewee.admin import Admin, ModelAdmin, AdminPanel
from flask_peewee.filters import QueryFilter
from wtforms.fields import FileField, HiddenField
from wtforms.form import Form

from peewee import fn
from app import app, db
from auth import auth
from models import User, Note, Tag, Photo, PhotoTags, Articles


class NotePanel(AdminPanel):
    template_name = 'admin/note/notes.html'


    def get_context(self):
        return {
            'note': "Welcome"
        }

class ArticlesAdmin(ModelAdmin):
    columns = ('pageid', 'title', 'created', 'iamap', 'published')
    
    
class NoteAdmin(ModelAdmin):
    columns = ('title', 'created',)
    
    
    def get_template_overrides(self):
        # override the edit template with a custom one
        return {'add': 'admin/note/add.html', 'edit': 'admin/note/edit.html'}   

class Article_Custom_Admin(ModelAdmin):
    columns = ('pageid', 'title', 'created', 'iamap', 'published')  
    
    def get_template_overrides(self):
        # override the edit template with a custom one
        return {'add': 'admin/articles/add.html', 'edit': 'admin/articles/edit.html'}   		

    
    
class PhotoAdmin(ModelAdmin):
    columns = ['name','image', 'thumb']

    def get_form(self, adding=False):
        class PhotoForm(Form):
            image = HiddenField()
            image_file = FileField(u'Image file')

        return PhotoForm

    def save_model(self, instance, form, adding=False):
        instance = super(PhotoAdmin, self).save_model(instance, form, adding)
        if 'image_file' in request.files:
            file = request.files['image_file']
            instance.save_image(file)

        return instance
    
class TagAdmin(ModelAdmin):
    columns = ['tag']
    
class PhotoTagsAdmin(ModelAdmin):
     columns = ['tags', 'photo']
    

    
admin = Admin(app,auth)

auth.register_admin(admin)
admin.register(Note, NoteAdmin)
admin.register(Articles,Article_Custom_Admin)
admin.register(Photo, PhotoAdmin)
admin.register(Tag, TagAdmin)
admin.register(PhotoTags, PhotoTagsAdmin)
admin.register_panel('Notes', NotePanel)


