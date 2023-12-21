from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql' ,
        'NAME': 'blog4', #Cambiar según nombre de la base de datos local
        'USER': 'root', #Cambiar según usuario de sql local
        'PASSWORD': 'maxi3624146625', #Cambiar según contraseña de sql local
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

