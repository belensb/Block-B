# vista basada en una funcion# 
from django.shortcuts import render


def index_view(request): #definimos el index_view y le hacemos un request para que solicite el archivo 
 return render(request, 'index.html', {}) #retornamos la solicitud y le pedimos que haga el render

def publicaciones_view(request): #definimos publicaciones y le hacemos la peticion con el request
    return render (request, 'publicaciones.html', {}) #hacemos el retorno de la peticion que hizo el request con ell render 
