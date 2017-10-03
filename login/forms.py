from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models as m
from django.contrib import auth


class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = m.Persona
        fields = (
            'curp',
            'rfc',
            'fechaDeNacimiento',
            'estadoCivil',
            'idRol',
        )

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = User
        fields=(
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
        )

    def save(self,commit=True):
        user= super(UserForm,self).save(commit=False)
        if commit:
            user.save()
            return  user
