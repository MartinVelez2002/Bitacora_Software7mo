from django.urls import path
from modulos.Actividades.views_actividades.view_actividades import *

app_name = 'actividad'

urlpatterns = [
    path('modulos_actividad/',(mostrarModulos.as_view()),name='modulos_actividad'),
    path('crear_actividad/', (anadirActividad.as_view()), name='crear_actividad'),
    path('listar_actividad/', (mostrarActividad.as_view()), name='listar_actividades'),
    path('editar_actividad<int:pk>', (editarActividad.as_view()), name='editar_actividad'),
    path('eliminar_actividad<int:pk>', (eliminarActividad.as_view()), name="eliminar_actividad")
]