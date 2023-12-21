from django import forms #importamos el módulo forms
from .models import Publicacion, Comentario  #importamos la tabla con la que vamos a trabajar 

class PublicarForm(forms.ModelForm): #definimos clase padre para heredar
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria']
        

class ComentarioForm(forms.ModelForm): 
    class Meta:
        model = Comentario
        fields = ['texto']