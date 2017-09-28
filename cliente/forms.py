from django import forms
from . import models as m

class ClienteForm(forms.ModelForm):
    class Meta:
        model = m.AsesorCliente(
            
        )
