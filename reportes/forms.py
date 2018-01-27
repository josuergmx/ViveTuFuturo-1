from django import forms
from productos import models as m

'''class institucionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(institucionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['nombre'].label = "Nombre de la Institución"
    class Meta:
        model = m.InstitucionFinanciera
        fields = (
            "nombre",
        )

class departamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(departamentoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['nombre'].label = "Nombre del Departamento"
    class Meta:
        model = m.Departamento
        fields = (
            "nombre",
        )

class planForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(planForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['nombre'].label = "Nombre del Producto"
    class Meta:
        model = m.Servicio
        fields = (
            "nombrePlan",
        )'''
    #institucion = forms.ModelChoiceField(queryset = InstitucionFinanciera.objects.all())
    #departamento = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
    #plan = forms.ModelChoiceField(queryset=InstitucionFinanciera.objects.all(), required=False)
