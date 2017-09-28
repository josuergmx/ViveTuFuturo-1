from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import forms as f
from . import models as m_l
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
    return redirect("namespace:unaurl")
"""
def login(request):
    print("tipo",request.method)
    if request.method == 'POST':
        form = f.loginForm(request.POST or None)
        usuario = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=usuario,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect('login:hola')
        else:
            context = {
                "mensaje":"Algo salio mal, ingresa de nuevo tus datos",
                "form":f.loginForm(),
            }
            return render(request,'log/login.html',context)

    return render(request,"log/login.html",{"form":f.loginForm()})

def logout(request):
    auth.logout(request)
    return render(request,"ok.html",{})

@login_required(redirect_field_name='login:login')
def hola(request):
    print("hola")
    return render(request,"perfil/dashboard.html")


@login_required(redirect_field_name='login:login')
def perfil(request):
    print("estoy dentro")
    return render(request,"perfil/perfil.html")



def registrar(request):
    if request.method == 'POST':
        form = f.UserForm(request.POST)
        formPersona = f.PersonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(m_l.EstadoCivil.objects.get(idEstadoCivil=1))
            estado = m_l.EstadoCivil.objects.get(idEstadoCivil=request.POST.get("estadoCivil",None))
            rol = m_l.Roles.objects.get(idRole=request.POST.get("idRol",None))
            m_l.Persona.objects.filter(user_id=user).update(
                estadoCivil = estado,
                folio = request.POST.get("folio",None),
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
