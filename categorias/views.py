from django.shortcuts import render

# Create your views here.
def categorias_view(request): #definimos el categorias_view y le hacemos un request para que solicite el archivo
 return render(request, 'categorias.html', {}) #retornamos la solicitud y le pedimos que haga el render

def romance_view(request): #definimos el romance_view y le hacemos un request para que solicite el archivo
 return render(request, 'romance.html', {}) #retornamos la solicitud y le pedimos que haga el render

def terror_view(request): #definimos el terror_view y le hacemos un request para que solicite el archivo
 return render(request, 'terror.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ficcion_view(request): #definimos el ficcion_view y le hacemos un request para que solicite el archivo
 return render(request, 'ficcion.html', {}) #retornamos la solicitud y le pedimos que haga el render

def ciencia_view(request): #definimos el ciencia_view y le hacemos un request para que solicite el archivo
 return render(request, 'ciencia.html', {}) #retornamos la solicitud y le pedimos que haga el render

def historia_view(request): #definimos el historia_view y le hacemos un request para que solicite el archivo
 return render(request, 'historia.html', {}) #retornamos la solicitud y le pedimos que haga el render

def guerra_view(request): #definimos el guerra_view y le hacemos un request para que solicite el archivo
 return render(request, 'guerra.html', {}) #retornamos la solicitud y le pedimos que haga el render
