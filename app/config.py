"""app/config.py
"""
import os

DEBUG = bool(int(os.getenv('DEBUG', '0')))
JSON_AS_ASCII = bool(int(os.getenv('JSON_AS_ASCII', '0')))
SECRET_KEY = os.getenv('SECRET_KEY', '')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', '')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
SQLALCHEMY_ECHO = bool(int(os.getenv('SQLALCHEMY_ECHO', '0')))
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': int(os.getenv("SQLALCHEMY_POOL_SIZE", '5')),
    'max_overflow': int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", '10')),
    'pool_timeout': int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", '30'))
}
SQLALCHEMY_TRACK_MODIFICATIONS = bool(
    int(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', '0')))
