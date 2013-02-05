# config
import os

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

class Configuration(object):
    DATABASE = {
        'name' : 'cmssql',
        'host' : '127.0.0.1',
        'port': 3306,
        'passwd' : 'test',
        'user' : 'root',
        'engine': 'peewee.MySQLDatabase',
    }
    DEBUG = True
    SECRET_KEY =  'development key'
    
    APP_ROOT = APP_ROOT
    MEDIA_ROOT = '%s/static/' % (APP_ROOT)
    
    # media settings for nginx / local
    MEDIA_URL = '/static'