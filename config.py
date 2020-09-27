import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'floppy174'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = '1'
    MAIL_USERNAME = 'es89645736668@gmail.com'
    MAIL_PASSWORD = 'energy3487715174s'
    ADMINS = ['es79645736668@gmail.com']
    LANGUAGES = ['en', 'ru']

    POSTS_PER_PAGE = 20