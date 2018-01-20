from django import forms
from productos.models import InstitucionFinanciera

class ReporteForm(forms.Form):
    periodoInicial = forms.DateField(widget=forms.DateInput())
    periodoFinal = forms.DateField(widget=forms.DateInput())
    institucion = forms.ModelChoiceField(queryset = InstitucionFinanciera.objects.all())
    departamento = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
    plan = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
