from django.db import models
from datetime import date

# Create your models here.
class Socio(models.Model):
    deportes = models.ManyToManyField('Deporte', related_name='socios')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, db_index=True)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    correo_electronico = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {'Activo' if self.activo else 'Inactivo'}"


class Deporte(models.Model):
    instalaciones = models.ManyToManyField('Instalacion', related_name='deportes')
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    cuota_mensual = models.DecimalField(max_digits=8, decimal_places=2, help_text="Cuota mensual para participar en este deporte.")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'No Disponible'
        return f"{self.nombre} - {estado}"


class Instalacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    necesita_reserva = models.BooleanField(default=False)
    horario_disponible = models.CharField(max_length=100, blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'No Disponible'
        return f"{self.nombre} ({estado})"
