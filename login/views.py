from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import forms as f
from . import models as m_l
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cliente import models as mCliente
# Create your views here.

"""
    return redirect("namespace:unaurl")
"""

def login(request):
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        return redirect('login:hola')
    else:
        if request.method == 'POST':
            usuario = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=usuario,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return redirect('login:hola')
            else:
                return render(request,'log/login.html',context)

        return render(request,"log/login.html",)


def logout(request):
    auth.logout(request)
    return redirect('principal')

@login_required(redirect_field_name='login:login')
def hola(request):
    asesorClientes = mCliente.AsesorCliente.objects.filter(idAsesor=request.user.id)
    n_clientes = len(asesorClientes)
    context = {
        "clientes":n_clientes
    }
    return render(request,"perfil/dashboard.html",context)

@login_required(redirect_field_name='login:login')
def registrar(request):
    if request.method == 'POST':
        form = f.UserForm(request.POST)
        formPersona = f.PersonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            estado = m_l.EstadoCivil.objects.get(idEstadoCivil=request.POST.get("estadoCivil",None))
            rol = m_l.Roles.objects.get(idRole=request.POST.get("idRol",None))
            m_l.Persona.objects.filter(user_id=user).update(
                estadoCivil = estado,
                curp = request.POST.get("curp",None),
                rfc = request.POST.get("rfc",None),
                fechaDeNacimiento = request.POST.get("fechaDeNacimiento",None),
            )
            persona = m_l.Persona.objects.get(user_id=user)
            persona.idRol.add(rol)
            return redirect('login:hola')
        else:
            form = f.UserForm()
            persona = f.PersonaForm()
            context = {
                "user":form,
                "persona":persona,
                "mensaje":"Error",
            }
            return render(request,"registar.html",context)
    else:
        form = f.UserForm()
        persona = f.PersonaForm()
        context = {
            "user":form,
            "persona":persona,
        }
        return render(request,"registar.html",context)
