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
            self.fields['idTipoCita'].label = "Tipo de cita"
            self.fields['idEstatus'].label = "Estado de la cita"
            self.fields['direccionCita'].label = "Direcion de la cita (en caso de ser presencial)"
            self.fields['link'].label = "Link de la cita (en caso de ser por videollamada)"
            self.fields['password'].label = "Password"
    class Meta:
        model = m.Cita
        fields = (
            "idTipoCita",
            "idEstatus",
            "fecha",
            "direccionCita",
            "link",
            "password",
            "descripcion"
        )
        widgets = {
            'fecha': SelectDateWidget,
        }
