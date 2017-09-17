from django.shortcuts import render
from . import forms as f
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Sale,Creditos
from django.conf import settings

@csrf_protect
def index(request):
    if request.method == 'GET':
        return render(request, 'cargo.html')
    else:
        token_id = request.POST["conektaTokenId"]
        sale = Sale()
        if token_id: #Prevents send empty token
            cantidad = int(request.POST.get("cantidad",None))
            for x in range(0,cantidad):
                Creditos.save()
            return HttpResponse(sale.charge(15, token_id))


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
