from django.db import models
from django.utils.timezone import now

# Create your models here.
class ActividadModel(models.Model):
    nombre_actividad = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(default=now)
    fecha_fin = models.DateTimeField(default=None)
    num_horas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_actividad}, {self.num_horas}"