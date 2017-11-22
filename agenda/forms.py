from django import forms
from . import models as m
from django.forms.extras.widgets import SelectDateWidget

class agendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(agendaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = m.Cita
        fields = (
            "idTipoCita",
            "idEstatus",
            "fecha",
            "direccionCita",
            "descripcion"
        )
        widgets = {
            'fecha': SelectDateWidget,
        }
