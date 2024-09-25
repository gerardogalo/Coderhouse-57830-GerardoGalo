from django.contrib import admin
from .models import Socio, Deporte, Instalacion

# Register your models here.

#admin.site.register(Socio)
#admin.site.register(Deporte)
#admin.site.register(Instalacion)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('apellido','nombre', 'correo_electronico', 'activo','edad')
    list_filter = ('activo',)
    search_fields = ('nombre', 'apellido', 'correo_electronico')
    ordering = ('apellido', 'nombre')

    def edad(self, obj):
        return obj.edad()
    edad.short_description = 'Edad'

@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuota_mensual', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Instalacion)
class InstalacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'necesita_reserva', 'disponible')
    list_filter = ('disponible', 'necesita_reserva')
    search_fields = ('nombre',)
    ordering = ('-capacidad',)
