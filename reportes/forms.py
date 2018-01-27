from django import forms
from productos.models import InstitucionFinanciera

class ReporteForm(forms.Form):
    institucion = forms.ModelChoiceField(queryset = InstitucionFinanciera.objects.all())
    departamento = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
    plan = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
