from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql' ,
        'NAME': '', #Cambiar según nombre de la base de datos local
        'USER': 'root', #Cambiar según usuario de sql local
        'PASSWORD': '', #Cambiar según contraseña de sql local
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

