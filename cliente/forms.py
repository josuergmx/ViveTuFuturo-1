from django import forms
from . import models as m
from login import models as mLogin
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = m.AsesorCliente
        fields = (
            "clienteProspecto",
            "Origen",
            "Estatus",
        )


class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = mLogin.Persona
        fields = (
            'curp',
            'rfc',
            'fechaDeNacimiento',
            'estadoCivil',
        )


class DireccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DireccionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['numinterior'].label = 'Numero Interior'
            self.fields['numexterior'].label = 'Numero Exterior'
            self.fields['idtipodireccion'].label = 'Lugar de Direccion'
    class Meta:
        model = mLogin.Direccion
        fields = (
            'idtipodireccion',
            'calle',
            'colonia',
            'delegacion',
            'cp',
            'numinterior',
            'numexterior',
        )


class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['email'].widget.attrs = {
                'placeholder':'user@email.com',
                'class': 'form-control'
            }
            self.fields['facebookid'].label = 'Facebook'
            self.fields['telcasa'].label = 'Telefono de Casa'
            self.fields['oficina'].label = 'Telefono de Oficina'
            self.fields['email'].label = 'Segundo Email'
    class Meta:
        model = mLogin.Contacto
        fields = (
            'celular',
            'email',
            'telcasa',
            'oficina',
            'facebookid',
        )
