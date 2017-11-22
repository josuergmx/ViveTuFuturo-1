from django import forms
INSTITUCIONES = (
    ('smnyl', "Seguros Monterrey"),
    ('allianz', "Allianz"),
)
PLANES = (
    ('plana', "Plan A"),
    ('planb', "Plan B"),
)
class ReporteVentasForm(forms.Form):
    periodoInicial = forms.DateField(label=u'Periodo Inicial', input_formats='%D/%M/%Y', required=True, widget=forms.DateInput(format = '%D/%M/%Y'))
    periodoFinal = forms.DateField(label=u'Periodo Final', input_formats='%D/%M/%Y', required=True, widget=forms.DateInput(format = '%D/%M/%Y'))
    institucion = forms.ChoiceField(choices=INSTITUCIONES)
    plan = forms.ChoiceField(choices=PLANES)

    def cleaned_periodoInicial(self):
        periodoInicial = self.cleaned_data.get("periodoInicial")
        if(len(periodoInicial) < 8 or len(periodoInicial) > 10 ):
            raise forms.ValidationError("El periodo inicial debe tener el formato dd/mm/yyyy")
        else:
            return periodoInicial

    def cleaned_periodoFinal(self):
        periodoFinal = self.cleaned_data.get("periodoFinal")
        if(len(periodoFinal) < 8 or len(periodoFinal) > 10 ):
            raise forms.ValidationError("El periodo final debe tener el formato dd/mm/yyyy")
        else:
            return periodoFinal

    def cleaned_institucion(self):
        institucion = self.cleaned_data.get("institucion")
        if(len(institucion) == 0 or institucion == None):
            raise forms.ValidationError("No se ha seleccionado ninguna institucion financiera")
        else:
            return institucion

    def cleaned_plan(self):
        plan = self.cleaned_data.get("plan")
        if(len(plan) == 0 or plan == None):
            raise forms.ValidationError("No se ha seleccionado ningun plan")
        else:
            return plan
