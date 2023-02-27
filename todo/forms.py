from django.forms import ModelForm
from .models import Tareas
from django import forms


class TareasForm(ModelForm):
   
    class Meta:
        model = Tareas
        fields = [
            'titulo',
            'descripcion',
            'fecha_limite',
        ]
