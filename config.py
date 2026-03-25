import os
basedir = os.path.abspath(os.path.dirname(__file__))
# I don't understand this line to be honest

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
#tbh I still didn't get this line
# I understand that it's some kind of configuration but what's up with secret key idk
#same thing with sqlalchemy thing