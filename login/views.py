from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import forms as f
from login.models import models as login
from asesor.models import models as asesor
from django.contrib import auth

# Create your views here.

"""
    return redirect("namespace:unaurl")
"""
def login(request):
    print("tipo",request.method)
    if request.method == 'POST':
        form = f.loginForm(request.POST or None)
        print("\n\nsoy for ", form.clean)
        usuario = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=usuario,password=password)
        print(user)
        if user is not None and user.is_active:
            print(auth.login(request,user))
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

def hola(request):
    return render(request,"hola.html",)

def registrar(request):
    if request.method == 'POST':
        form = f.UserForm(request.POST)
        formPersona = f.PersonaForm(request.POST)
        if form.is_valid():
            user = form.save()
            estado = login.EstadoCivil.objects.get(idEstadoCivil=request.POST.get("estadoCivil",None))
            rol = login.Roles.objects.get(idRole=request.POST.get("idRol",None))
            m.Persona.objects.filter(user_id=user).update(
                estadoCivil = estado,
                folio = request.POST.get("folio",None),
                curp = request.POST.get("curp",None),
                rfc = request.POST.get("rfc",None),
                fechaDeNacimiento = request.POST.get("fechaDeNacimiento",None),
            )
            persona = login.Persona.objects.get(user_id=user)
            persona.idRol.add(rol)
            return render(request,'ok.html')
        else:
            messages.error(request, "An Error Occured !")

    else:
        form = f.UserForm()
        persona = f.PersonaForm()
        context = {
            "user":form,
            "persona":persona,
        }
        return render(request,"registar.html",context)
