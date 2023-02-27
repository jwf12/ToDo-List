from django.contrib import admin
from .models import Tareas


class TareasAdmin(admin.ModelAdmin):
    list_display = ('usuario',
                    'titulo',
                    'descripcion',
                    'fecha_inicio',
                    'fecha_limite',
                    'status',
                    )

admin.site.register(Tareas, TareasAdmin)

