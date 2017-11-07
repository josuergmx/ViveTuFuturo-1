from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from promotor.models import promotorAsesor
from django.contrib import auth


class promotorAsesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(promotorAsesorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = promotorAsesor
        fields = (
            'institucion',
        )
