from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario) #Registramos el modelo Usuario para que esté disponible desde el panel de admin