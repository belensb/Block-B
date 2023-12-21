from typing import Any
from django.shortcuts import render, redirect
from .models import Publicacion,  Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from .forms import PublicarForm, ComentarioForm

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
    
    def form_valid(self, form):
       f = form.save(commit=False) #acá se detiene el formulario para que no guarde
       f.creador_id = self.request.user.id
       return super().form_valid(f)
   
    def get_success_url(self):
       return reverse('publicaciones')


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
   
#view para ver a detalle una publicacion
class DetallePublicacionView(DetailView):
    model=Publicacion
    template_name = 'publicaciones/detalle.html'
    context_object_name = 'publicacion'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context
    
    
    
    def post(self, request, *args, **kwargs):
       
        publicacion = self.get_object()
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador_id = self.request.user.id
            comentario.publicacion = publicacion 
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)