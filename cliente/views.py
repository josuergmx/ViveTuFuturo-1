from django.shortcuts import render,redirect
from django.contrib.auth import get_user
from . import forms as f
from . import models as m
from login import forms as fLogin
from login import models as mLogin
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name='login:login')
def agregarCliente(request):
    if request.user.persona.idRol == 1:
        return render(request,"login/login",)
    else:
        if request.method == 'POST':
            usuario = fLogin.UserForm(request.POST)
            persona = f.PersonaForm(request.POST)
            cliente = f.ClienteForm(request.POST)
            print(usuario.is_valid())
            print(request.POST)
            if usuario.is_valid():
                user = usuario.save()
                estado = mLogin.EstadoCivil.objects.get(idEstadoCivil=request.POST.get("estadoCivil",None))
                rol = mLogin.Roles.objects.get(idRole=1)
                fecha = request.POST.get("fechaDeNacimiento",None)
                cliente = mLogin.User.objects.get(username=request.POST.get("username"))
                persona = mLogin.Persona.objects.get(user_id=user)
                tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion=request.POST.get("idtipodireccion",None))
                if request.POST.get("clienteProspecto",None) == "on":
                    prospecto = True
                else:
                    prospecto = False
                mLogin.Persona.objects.filter(user_id=user).update(
                    estadoCivil = estado,
                    fechaDeNacimiento = fecha,
                    idRol = rol,
                    curp = request.POST.get("curp",None),
                    rfc = request.POST.get("rfc",None),
                )
                cliente = m.AsesorCliente(
                    idCliente   = persona,
                    idAsesor    = get_user(request),
                    clienteProspecto = prospecto,
                    Origen  = m.OrigenRecomendacion.objects.get(idOrigen=request.POST.get("estadoCivil",None)),
                    Estatus = m.Estatus.objects.get(idEstatus=request.POST.get("Estatus",None)),
                    fechaActualizacion = date.today(),
                )
                direccion = mLogin.Direccion(
                    idpersona = persona,
                    idtipodireccion = tipodireccion,
                    calle = request.POST.get("calle",None),
                    colonia = request.POST.get("colonia",None),
                    delegacion = request.POST.get("delegacion",None),
                    cp = request.POST.get("cp",None),
                    numinterior = request.POST.get("numinterior",None),
                    numexterior = request.POST.get("numexterior",None),
                )
                contacto = mLogin.Contacto(
                    idpersona = persona,
                    celular = request.POST.get("celular",None),
                    email = request.POST.get("email",None),
                    telcasa = request.POST.get("telcasa",None),
                    oficina = request.POST.get("oficina",None),
                    facebookid = request.POST.get("facebookid",None),
                )
                cliente.save()
                contacto.save()
                direccion.save()
                return redirect('cliente:agregarCliente')
        else:
            usuario = fLogin.UserForm()
            persona = f.PersonaForm()
            cliente = f.ClienteForm()
            direccion = f.DireccionForm()
            contacto = f.ContactoForm()
            context = {
                "usuario":usuario,
                "persona":persona,
                "cliente":cliente,
                "contacto":contacto,
                "direccion":direccion,
            }
            return render(request,"cliente/cliente_add.html",context)

@login_required(redirect_field_name='login:login')
def clientes(request):
    asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
    contactos = []
    direcciones = []
    for c in asesorClientes:
        print(c.idCliente.contacto.all())
        contactol = mLogin.Contacto.objects.filter(idpersona=c.idCliente)
        direccionl = mLogin.Direccion.objects.filter(idpersona=c.idCliente)
        contactos.append(contactol)
        direcciones.append(direccionl)

    context = {
        "clientes":asesorClientes,
        "contactos":contactos,
        "direcciones":direcciones,
    }
    return render(request,"cliente/cliente_show.html",context)

@login_required(redirect_field_name='login:login')
def gestionarClientes(request):
    return render(request,"cliente/cliente_gestionar.html")
