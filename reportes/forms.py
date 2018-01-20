from django import forms
from .models import Institucionfinanciera

class ReporteForm(forms.Form):
    periodoInicial = forms.DateField(widget=forms.DateInput())
    periodoFinal = forms.DateField(widget=forms.DateInput())
    institucion = forms.ModelChoiceField(queryset = Institucionfinanciera.objects.all())
    departamento = forms.ModelChoiceField(queryset=Institucionfinanciera.objects.all(), required=False)
    plan = forms.ModelChoiceField(queryset=Institucionfinanciera.objects.all(), required=False)
