from .base import *
from decouple import config

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Datos db producción, modificar en el archivo .env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}