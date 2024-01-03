from django.urls import reverse_lazy
from django.views.generic import *
from modulos.Docentes.forms import FormDocentes
from modulos.Docentes.models import DocentesModel
from django.contrib.auth.mixins import LoginRequiredMixin

class modulosDocentes(LoginRequiredMixin, TemplateView):
    template_name = 'modulos_docente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = ''


class mostrarListado(LoginRequiredMixin, ListView):
    model = DocentesModel
    template_name = 'detalle_docente.html'
    context_object_name = 'docentes'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_list'] = 'Docentes Registrados'
        return context


class anadirDocente(LoginRequiredMixin, CreateView):
    model = DocentesModel
    template_name = '../Templates/docentes_añadir.html'
    success_url = reverse_lazy('docentes:listar_docentes')
    form_class = FormDocentes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Agregar Docentes'
        context['url_anterior'] = '/docentes/modulos_docentes/'

        return context


class EditarDocente(LoginRequiredMixin, UpdateView):
    model = DocentesModel
    template_name = 'editar_docente.html'
    success_url = reverse_lazy('docentes:listar_docentes')
    form_class = FormDocentes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Edición de Docentes'
        context['url_anterior'] = '/docentes/listar_docentes/'

        return context


class EliminarDocente(LoginRequiredMixin, DeleteView):
    model = DocentesModel
    template_name = 'eliminar_docente.html'
    success_url = reverse_lazy('docentes:listar_docentes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo_add'] = 'Eliminar Docente'
        context['url_anterior'] = '/docentes/listar_docentes'

        return context
