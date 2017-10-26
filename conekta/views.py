from django.shortcuts import render
from . import forms as f
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Sale,Creditos
from . import models as m
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@csrf_protect
@login_required(redirect_field_name='login:login')
def index(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == 'GET':
            return render(request, 'conekta/main.html')
        else:
            token_id = request.POST.get("conektaTokenId",False)
            sale = Sale()
            print(token_id)
            if token_id: #Prevents send empty token
                cantidad = int(request.POST.get("cantidad",None))
                for x in range(0,cantidad):
                    estatus = m.Estatuscredito.objects.get(nombre="Sin asignar")
                    credito = Creditos(
                        idAsesor=request.user.persona,
                        estatusCredito=estatus
                    )
                    credito.save()
                return HttpResponse(sale.charge(token_id,cantidad))
    else:
        raise PermissionDenied

# Create your views here.
@login_required(redirect_field_name='login:login')
def crearOrden(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
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
                return render(request,"conekta/orden.html",context)
        else:
            orden = f.CrearOrden()
            context = {
                "hola":"hola"
            }
            return render(request,"conekta/main.html",context)
    else:
        raise PermissionDenied
