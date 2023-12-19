from django.urls import path #importamos los path desde django urls
from .import views #importamos las views 


urlpatterns = [
    path('registrarse/', views.RegistrarseView.as_view(), name='registrarse')
    ]   