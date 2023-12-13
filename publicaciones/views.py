from django.shortcuts import render
from .models import Publicacion

# Crea tus vistas aqui.

def publicaciones_view(request):  #definimos el publicaciones_view y le hacemos un request para que solicite el archivo
 #creamos una variable a la que se le asigan un diccionario que se utilizará para traer los datos de la db
 ctx = {
  'publicaciones' : Publicacion.objects.all().order_by('fecha') #hacemos la solicitud para que la db nos devuelva todo de la tabla publicaciones
 }

 return render(request, 'publicaciones.html', ctx) #retornamos la solicitud y le pedimos que haga el render

