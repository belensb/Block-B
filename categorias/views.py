from django.shortcuts import render

# Create your views here.
def categorias_view(request): #definimos el terror_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias.html', {}) #retornamos la solicitud y le pedimos que haga el render

def romance_view(request): #definimos el romance_view y le hacemos un request para que solicite el archivo
 return render(request, 'romance.html', {}) #retornamos la solicitud y le pedimos que haga el render

def terror_view(request): #definimos el fabula_view y le hacemos un request para que solicite el archivo
 return render(request, 'terror.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ficcion_view(request): #definimos el fabula_view y le hacemos un request para que solicite el archivo
 return render(request, 'ficcion.html', {}) #retornamos la solicitud y le pedimos que haga el render

