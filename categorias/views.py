from django.shortcuts import render
from publicaciones.models import Publicacion

# Create your views here.
def categorias_view(request): #definimos el categorias_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias/categorias.html', {}) #retornamos la solicitud y le pedimos que haga el render

def publicaciones_por_categoria(request, nombre_categoria):
    # Filtrar las publicaciones por la categoría
    publicaciones = Publicacion.objects.filter(categoria__nombre=nombre_categoria)

    return render(request, 'categorias/publicaciones_por_categoria.html', {'publicaciones': publicaciones})