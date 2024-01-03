from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from modulos.Actividades.forms import FormActividades
from modulos.Actividades.models import ActividadModel


class mostrarModulos(LoginRequiredMixin, TemplateView):
    template_name = 'modulos_actividades.html'


class anadirActividad(LoginRequiredMixin, CreateView):
    model = ActividadModel
    template_name = 'anadir_actividad.html'
    success_url = reverse_lazy('actividad:listar_actividades')
    form_class = FormActividades

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Crear Actividad'
        context['url_anterior'] = '/'

        return context


class mostrarActividad(LoginRequiredMixin, ListView):
    model = ActividadModel
    template_name = 'listar_actividades.html'
    context_object_name = 'actividades'


class editarActividad(LoginRequiredMixin, UpdateView):
    model = ActividadModel
    template_name = 'editar_actividad.html'
    success_url = reverse_lazy('actividad:listar_actividades')
    form_class = FormActividades

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['url_anterior'] = '/actividad/listar_actividad'

        return context

class eliminarActividad(LoginRequiredMixin, DeleteView):
    model = ActividadModel
    template_name = 'eliminar_actividad.html'
    success_url = reverse_lazy('actividad:listar_actividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['url_anterior'] = '/actividad/listar_actividad'
        context['titulo_add'] = 'Eliminar actividad'


        return context