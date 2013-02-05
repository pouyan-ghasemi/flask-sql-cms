from app import app, db

from auth import *
from admin import admin
from models import *
from views import *

admin.setup()


if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Note.create_table(fail_silently=True)
    Tag.create_table(fail_silently=True)
    Photo.create_table(fail_silently=True)
    PhotoTags.create_table(fail_silently=True)
    Articles.create_table(fail_silently=True)
    app.run()
