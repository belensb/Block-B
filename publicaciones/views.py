from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PublicarForm #importamos el formulario para publicar

# Crea tus vistas aqui.

def Publicaciones_view(request):  #definimos el publicaciones_view y le hacemos un request para que solicite el archivo
 #creamos una variable a la que se le asigan un diccionario que se utilizará para traer los datos de la db
 ctx = {
  'publicaciones' : Publicacion.objects.all() #hacemos la solicitud para que la db nos devuelva todo de la tabla publicaciones
 }

 return render(request, 'publicaciones/publicaciones.html', ctx) #retornamos la solicitud y le pedimos que haga el render

#view basada en clase, para enlistar las publicaciones
class PublicacionesView(ListView):
    template_name = 'publicaciones.html'
    model = Publicacion 
    context_object_name = 'publicaciones'


#view basada en clase para crear una publucación
class Publicar(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = PublicarForm


#view basada en una clase para modificar publicaciones
class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones/'
    
    
#view basada en una clase para eliminar una publicación
class EliminarPublicacionView(DeleteView):
   model = Publicacion
   template_name = 'publicaciones/eliminar-publicacion.html'
   success_url = '../ver-publicaciones/'