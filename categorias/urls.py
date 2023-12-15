from django.urls import path
from . import views #importamos los views

urlpatterns = [
    path ('ver-categorias/', views.categorias_view, name='ver-categorias'),
    path('intro-romance/', views.romance_view, name='romance'),
    path('intro-terror/', views.terror_view, name='terror'),
    path('intro-ficcion/', views.ficcion_view, name='ficcion'),
]

"""path('romance/', views.romance_view, name='romance'),"""