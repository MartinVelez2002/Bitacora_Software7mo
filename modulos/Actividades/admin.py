from django.contrib import admin
from modulos.Docentes.models import *
from modulos.Actividades.models import *
from modulos.Bitacora.models import *


# Register your models here.
admin.site.register(DocentesModel)
admin.site.register(ActividadModel)
admin.site.register(bitacoraModelCabecera)
admin.site.register(bitacoraModelDetalle)

