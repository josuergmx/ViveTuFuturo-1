from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models as m
from django.contrib import auth


class PersonaForm(forms.ModelForm):
    class Meta:
        model = m.Persona
        fields = (
            'folio',
            'curp',
            'rfc',
            'fechaDeNacimiento',
            'estadoCivil',
            'idRol',
        )

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
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


class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'password'}))

    def clean(self,*args,**kwargs):
        if username and password:
            username = self.cleaned_data.get['username']
            password = self.cleaned_data.get['password']
            user = auth.authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError('No existe el usuario')

            if user.check_password(password):
                raise forms.ValidationError('No exist la cotraseña')

            if user.is_active:
                raise forms.ValidationError('No estas activo')

        return super(loginForm,self).clean(*args, **kwargs)
