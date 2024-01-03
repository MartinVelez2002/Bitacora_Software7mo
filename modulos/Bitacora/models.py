from django.db import models
from modulos.Actividades.models import *
from modulos.Docentes.models import *
from django.utils.timezone import now

# Create your models here.

class bitacoraModelCabecera(models.Model):
    nombre = models.ForeignKey(DocentesModel, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.nombre)
class bitacoraModelDetalle(models.Model):
    nombre_actividad = models.ForeignKey(ActividadModel, on_delete=models.PROTECT, related_name='actividades_relacionadas')
    horas = models.ForeignKey(ActividadModel, on_delete=models.PROTECT, blank=True, null=True, related_name='horas_relacionadas')
    evidencia = models.FileField(upload_to='evidencias', blank=True, null=True)


