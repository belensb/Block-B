from django.urls import path #importamos los path desde django urls
from .import views #importamos las views 


urlpatterns = [
    path ('ver-publicaciones/', views.Publicaciones_view, name='publicaciones'), #enlazamos ver-publicaciones con las views y le damos el nombre ver-publicaciones
    path('publicar/', views.Publicar.as_view(), name ='publicar'),
    path ('modificar/<int:pk>', views.ModificarPublicacionView.as_view(),name= 'modificar-publicacion'),
    path('eliminar/<int:pk>', views.EliminarPublicacionView.as_view(),name='eliminar-publicacion'),
    path('detalle/<int:pk>', views.DetallePublicacionView.as_view(),name='detalle-publicaciones'),
    ]   