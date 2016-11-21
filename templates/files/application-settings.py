# -*- coding: utf-8 -*-
import os
from project.settings import *

gettext = lambda s: s
_ = gettext

COMPRESS_ENABLED = True
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*',]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '{{ audiokitt_server_secret_key }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ audiokitt_db_name }}',
        'USER': '{{ audiokitt_db_username }}',
        'PASSWORD': '{{ audiokitt_db_password }}',
        'HOST': '{{ audiokitt_db_host }}',
        'PORT': '{{ audiokitt_db_port }}',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}