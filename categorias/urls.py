from django.urls import path
from . import views #importamos los views

urlpatterns = [
    path ('ver-categorias/', views.categorias_view, name='ver-categorias'),
    path('<str:nombre_categoria>/', views.publicaciones_por_categoria, name='publicaciones_por_categoria'),
]

"""path('romance/', views.romance_view, name='romance'),"""