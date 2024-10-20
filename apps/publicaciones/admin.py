from django.contrib import admin
from .models import Publicacion, Categoria, Comentario
# Register your models here.
admin.site.register(Publicacion) #Registramos el modelo Publicacion para que esté disponible desde el panel de admin
admin.site.register(Categoria) #Registramos el modelo Categoria para que esté disponible desde el panel de admin
admin.site.register(Comentario) #Registramos el modelo Comentario para que esté disponible desde el panel de admin