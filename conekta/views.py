from django.shortcuts import render
from . import forms as f
import conekta

conekta.locale = 'es'

# Create your views here.
def crearOrden(request):

    if request.method == 'POST':
        orden = f.CrearOrden(request.POST or None)
        if orden.is_valid():
            tarjeta = orden.cleaned_data.get['tarjeta']
            monto = orden.cleaned_data.get['monto']
            cantidad = orden.cleaned_data.get['cantidad']

        else:
            mensaje = "No debe olvidar poner su tarjeta"
            context = {
                'mensaje':mensaje,
                'form':f.CrearOrden()
            }
            return render(request,"conecta/orden.html",context)
    else:
        orden = f.CrearOrden()
        context = {
            "hola":"hola"
        }
        return render(request,"conecta/orden.html",context)
