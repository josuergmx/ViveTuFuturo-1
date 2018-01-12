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

class RecomendadoClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecomendadoClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = m.RecomendadoCliente
        fields = (
            "nombre",
            "celular",
            "estadoCivil",
            "hijos",
        )

class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['curp'].widget.attrs = {
                'class': 'form-control',
                'maxlength' : '18'
            }
            self.fields['rfc'].widget.attrs = {
                'class': 'form-control',
                'maxlength' : '13'
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
            self.fields['cp'].widget.attrs = {
                'class': 'form-control',
                'maxlength' : '5'
            }
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
            self.fields['celular'].widget.attrs = {
                'class': 'form-control',
                'maxlength':15,
                'type':'number',
            }

            self.fields['telcasa'].widget.attrs = {
                'class': 'form-control',
                'maxlength':15,
            }
            self.fields['facebookid'].label = 'Facebook'
            self.fields['telcasa'].label = 'Telefono de Casa'
            self.fields['oficina'].label = 'Telefono de Oficina'

    class Meta:
        model = mLogin.Contacto
        fields = (
            'celular',
            'telcasa',
            'oficina',
            'facebookid',
        )

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['email'].widget.attrs = {
                'placeholder':'user@email.com',
                'class': 'form-control',
            }
    class Meta:
        model = User
        fields=(
            'first_name',
            'last_name',
            'username',
            'email',
        )
