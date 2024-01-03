from django import forms
from django.forms import ModelForm
from modulos.Actividades.models import ActividadModel


class FormActividades(ModelForm):
    class Meta:
        model = ActividadModel
        fields = '__all__'
        widgets = {
            'nombre_actividad': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombreActividad'}),
            'fecha_inicio': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date', 'id': 'fechaInicio'}),
            'fecha_fin': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date', 'id': 'fechaFin'}),
            'num_horas': forms.NumberInput(attrs={'class': 'form-control', 'id': 'numHoras'}),

        }
