from django import forms
from django.forms import ModelForm
from modulos.Docentes.models import DocentesModel


class FormDocentes(ModelForm):
    class Meta:
        model = DocentesModel
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombreDocente'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'id': 'apellidoDocente  '}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'id': 'telefonoDocente'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'id': 'correoDocente'})

        }
