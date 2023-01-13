"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    DATABASE_USERNAME = environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')
    DATABASE_NAME = environ.get('DATABASE_NAME')
    DATABASE_ROOT_PASSWORD = environ.get('DATABASE_ROOT_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'mysql://druiz:fortisima@localhost:3306/todo-flask'
    # TODO: Solucionar error al pasar las variables de .env a la uri para conectarse a mysql
    # SQLALCHEMY_DATABASE_URI = f'mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:3306/{DATABASE_NAME}'.format(
    #    DATABASE_USER=DATABASE_USER, DATABASE_PASSWORD=DATABASE_PASSWORD, DATABASE_NAME=DATABASE_NAME)


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
