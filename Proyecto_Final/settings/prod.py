from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#Datos de la db en python anywhere, NO MODIFICAR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grupo6info$blog_db',
        'USER': 'grupo6info',
        'PASSWORD': 'informatorio2023',
        'HOST': 'grupo6info.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}