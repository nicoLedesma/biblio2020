from django.contrib import admin
from core.models import MateriaLectura

class MateriaLecturaAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'codigo', 'status']

    fieldsets = (
        ('Información del libro', {
            'fields': (
                'titulo', 'codigo', 'anio_publicacion', 'status',
            ),
        }),
        ('Informacion extra', {
            'fields': (
                'foto_portada', 'resumen',
            ),
        }),
    )



# Register your models here.
admin.site.register(MateriaLectura, MateriaLecturaAdmin)