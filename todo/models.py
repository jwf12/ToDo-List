from django.db import models
from django.contrib.auth.models import User


class Tareas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=205)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(auto_now=True)
    fecha_limite = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo