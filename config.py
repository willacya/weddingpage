import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'andrewwillacy@gmail.com'
    MAIL_PASSWORD = 'eejjutobtplpcuyc'
    ADMINS = ['andrewwillacy@gmail.com']
    LANGUAGES = ['en', 'es']
    POSTS_PER_PAGE = 25
"""

from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'andrewwillacy@gmail.com',
    "MAIL_PASSWORD": 'eejjutobtplpcuyc'
}

app.config.update(mail_settings)
mail = Mail(app)"""