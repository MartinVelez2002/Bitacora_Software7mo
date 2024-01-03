from django.db import models

class DocentesModel(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField(default=0)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

