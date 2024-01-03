"""
URL configuration for ecommerse project.

The `urlpatterns` list routes URLs to views_docentes. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views_docentes
    1. Add an import:  from my_app import views_docentes
    2. Add a URL to urlpatterns:  path('', views_docentes.home, name='home')
Class-based views_docentes
    1. Add an import:  from other_app.views_docentes import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from modulos.Docentes.views_docentes.views_docentes import *

app_name = 'docentes'
urlpatterns = [
    path('modulos_docentes/', (modulosDocentes.as_view()), name="modulos_docentes"),
    path('listar_docentes/', (mostrarListado.as_view()), name='listar_docentes'),
    path('crear_docente/', (anadirDocente.as_view()), name='agregar_docente'),
    path('editar_docente/<int:pk>', (EditarDocente.as_view()), name='editar_docente'),
    path('eliminar_docente/<int:pk>', (EliminarDocente.as_view()), name='eliminar_docente'),
]
