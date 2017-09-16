from django import forms

class CrearOrden(forms.Form):
    class Meta:
        tarjeta = forms.CharField(widget=forms.TextInput(attrs={'class':'','name':'tarjeta'}))
        monto = forms.CharField(widget=forms.PasswordInput(attrs={'name':'monto','value':'30'}))
