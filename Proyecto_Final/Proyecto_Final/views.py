# vista basada en una funcion# 
from django.shortcuts import render


def index_view(request): #definimos el index_view y le hacemos un request para que solicite el archivo 
 return render(request, 'index.html', {}) #retornamos la solicitud y le pedimos que haga el render 

