from django.urls import path #importamos los path desde django urls
from .import views #importamos las views 


urlpatterns = [
    path ('ver-publicaciones/', views.Publicaciones_view, name='publicaciones'), #enlazamos ver-publicaciones con las views y le damos el nombre ver-publicaciones
    path('publicar/', views.Publicar.as_view(), name ='publicar'),
    path ('modificar/<int:pk>', views.ModificarPublicacionView.as_view(),name= 'modificar-publicacion')
    
    ]   