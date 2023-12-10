from django.urls import path #importamos los path desde django urls
from .import views #importamos las views 


urlpatterns = [
    path ('ver-publicaciones/', views.publicaciones_view, name='ver-publicaciones') #enlazamos ver-publicaciones con las views y le damos el nombre ver-publicaciones
]   