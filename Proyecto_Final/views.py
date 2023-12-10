# vista basada en una funcion.
from django.shortcuts import render


def index_view(request): #definimos el index_view y le hacemos un request para que solicite el archivo
 return render(request, 'index.html', {}) #retornamos la solicitud y le pedimos que haga el rendet

def inicio_view(request): #definimos el terror_view y le hacemos un request para que solicite el archivo
 return render(request, 'inicio.html', {}) #retornamos la solicitud y le pedimos que haga el render


def romance_view(request): #definimos el romance_view y le hacemos un request para que solicite el archivo
 return render(request, 'romance.html', {}) #retornamos la solicitud y le pedimos que haga el render


def fabula_view(request): #definimos el fabula_view y le hacemos un request para que solicite el archivo
 return render(request, 'fabula.html', {}) #retornamos la solicitud y le pedimos que haga el render

def terror_view(request): #definimos el fabula_view y le hacemos un request para que solicite el archivo
 return render(request, 'terror.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ficcion_view(request): #definimos el fabula_view y le hacemos un request para que solicite el archivo
 return render(request, 'ficcion.html', {}) #retornamos la solicitud y le pedimos que haga el render