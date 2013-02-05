from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth


SECRET_KEY = 'development key'
DEBUG = True


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()




@app.route('/')
def index():
    return "CMS-SQL"


if __name__ == '__main__':
    app.run()
