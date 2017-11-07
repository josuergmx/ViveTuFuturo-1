from django.shortcuts import render
from . import forms as f
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Sale,Creditos
from . import models as m
from django.conf import settings
from django.contrib.auth.decorators import login_required

@csrf_protect
@login_required(redirect_field_name='login:login')
def orden(request):
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
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def index(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        n_creditos = m.Creditos.objects.filter(idAsesor=request.user)
        print(n_creditos)
        context = {
            "creditos":n_creditos,
        }
        return render(request,'conekta/creditos.html',context)
# Create your views here.
