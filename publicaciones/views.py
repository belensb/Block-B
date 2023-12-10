from django.shortcuts import render


# Crea tus vistas aqui.

def publicaciones_view(request):                  #definimos el publicaciones_view y le hacemos un request para que solicite el archivo
 return render(request, 'publicaciones.html', {}) #retornamos la solicitud y le pedimos que haga el render

