from django.shortcuts import render
from publicaciones.models import Publicacion

# Create your views here.
def categorias_view(request): #definimos el categorias_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/categorias.html', {}) #retornamos la solicitud y le pedimos que haga el render

def romance_view(request): #definimos el romance_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/romance.html', {}) #retornamos la solicitud y le pedimos que haga el render

def terror_view(request): #definimos el terror_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/terror.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ficcion_view(request): #definimos el ficcion_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/ficcion.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ciencia_view(request): #definimos el ciencia_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/ciencia.html', {}) #retornamos la solicitud y le pedimos que haga el render

def historia_view(request): #definimos el historia_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/historia.html', {}) #retornamos la solicitud y le pedimos que haga el render

def guerra_view(request): #definimos el guerra_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/guerra.html', {}) #retornamos la solicitud y le pedimos que haga el render

def publicaciones_por_categoria(request, nombre_categoria):
    # Filtrar las publicaciones por la categoría
    publicaciones = Publicacion.objects.filter(categoria__nombre=nombre_categoria)

    return render(request, 'categorias/publicaciones_por_categoria.html', {'publicaciones': publicaciones})