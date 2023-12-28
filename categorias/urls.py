from django.urls import path
from . import views #importamos los views

urlpatterns = [
    path ('ver-categorias/', views.categorias_view, name='ver-categorias'),
    path('intro-romance/', views.romance_view, name='romance'),
    path('intro-terror/', views.terror_view, name='terror'),
    path('intro-ficcion/', views.ficcion_view, name='ficcion'),
    path('intro-ciencia/', views.ciencia_view, name='ciencia'),
    path('intro-historia/', views.historia_view, name='historia'),
    path('intro-guerra/', views.guerra_view, name='guerra'),
    path('<str:nombre_categoria>/', views.publicaciones_por_categoria, name='publicaciones_por_categoria'),
]

"""path('romance/', views.romance_view, name='romance'),"""