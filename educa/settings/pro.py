from .base import *
from decouple import config

DEBUG = False

# When DEBUG is off and a view raises an exception, all info will be sent by email
# to people listed in the ADMINS setting.
ADMINS = (
    ('Suhail Ahmed', config("EMAIL")),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testblog',
        'USER': 'postgres',
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '8080',
    }
}
