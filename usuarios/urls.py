from django.urls import path #importamos los path desde django urls
from .import views #importamos las views 
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('registrarse/', views.RegistrarseView.as_view(), name='registrarse'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout')
    ]   