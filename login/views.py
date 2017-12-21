from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import forms as f
from . import models as m_l
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cliente import models as mCliente
from promotor import models as mPromotor
from creditos import models as mCreditos
from agenda import models as mCita
from datetime import datetime, timedelta

# Create your views here.
from django.views.defaults import page_not_found

"""
    return redirect("namespace:unaurl")
"""

def login(request):
    if request.user.is_authenticated():
        return redirect('login:hola')
    else:
        if request.method == 'POST':
            usuario = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=usuario,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                print(type(user.persona.idRol))
                if user.persona.idRol.idRole == 1: #cliente
                    return redirect('cliente:hola')
                else:
                    return redirect('login:hola')
            else:

                return redirect("login:login")
        return render(request,"log/login.html")


def logout(request):
    auth.logout(request)
    return redirect('principal')

@login_required(redirect_field_name='login:login')
def hola(request):
    #Vista del Asesor-promotor
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        n_clientes = 0
        n_asesores = 0
        citas = 0
        iterar = 0
        hoy = 0
        pendientes = []
        aux = datetime.today()+timedelta(7)
        semana = aux.strftime("%Y-%m-%d")
        dia = datetime.today().strftime("%Y-%m-%d")
        asesorClientes = mCliente.AsesorCliente.objects.filter(idAsesor=request.user.id)
        for i in asesorClientes:
            if i.activo == True:
                n_clientes = n_clientes + 1
            try:
                if i.fecha.strftime("%Y-%m-%d") >= dia:
                    citas = citas + 1
                if i.fecha.strftime("%Y-%m-%d") >= dia and i.fecha.strftime("%Y-%m-%d") <= semana:
                    pendientes.append(mCita.Cita.objects.get(idAsesorCliente=i,fecha=i.fecha))
                if i.fecha.strftime("%Y-%m-%d") == dia:
                    hoy = hoy + 1
            except:
                pass

            iterar = iterar+1

        if request.user.persona.idRol.idRole == 3: #agregamos la parte de gestionar asesores
            asesorPromotor = mPromotor.promotorAsesor.objects.filter(idPromotor=request.user.id)
            for i in asesorPromotor:
                if i.activo == True:
                    n_asesores = n_asesores + 1
        n_creditos = mCreditos.Creditos.objects.filter(idAsesor=request.user.id)
        recomendados = mCliente.RecomendadoCliente.objects.filter(asesor=request.user.persona)
        try:
            recomendados = recomendados[0:3]
        except:
            recomendados = recomendados
        context = {
            "recomendados":recomendados,
            "pendientes":pendientes,
            "rol":request.user.persona.idRol.idRole,
            "asesores":n_asesores,
            "clientes":n_clientes,
            "creditos":len(n_creditos),
            "citas":citas,
            "hoy":hoy,
        }
        return render(request,"perfil/dashboard.html",context)
    else: #Aqui va la vista del cliente
        return render(request,'log/404.html')
