from django.shortcuts import render,redirect
from django.contrib.auth import get_user
from . import forms as f
from . import models as m
from login import forms as fLogin
from login import models as mLogin
from datetime import date
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

@login_required(redirect_field_name='login:login')
def agregarCliente(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == 'POST':
            usuario = fLogin.UserForm(request.POST)
            persona = f.PersonaForm(request.POST)
            cliente = f.ClienteForm(request.POST)
            print(usuario.is_valid())
            print(request.POST)
            if usuario.is_valid() and persona.is_valid and cliente.is_valid():
                user = usuario.save()
                rol = mLogin.Roles.objects.get(idRole=1)
                fecha = request.POST.get("fechaDeNacimiento",None)
                persona = mLogin.Persona.objects.get(user_id=user)
                tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion=request.POST.get("idtipodireccion",None))
                estado = mLogin.EstadoCivil.objects.get(idEstadoCivil=request.POST.get("estadoCivil",None))
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
                clientec = m.AsesorCliente(
                    idCliente   = persona,
                    idAsesor    = get_user(request),
                    clienteProspecto = prospecto,
                    Origen  = m.OrigenRecomendacion.objects.get(idOrigen=request.POST.get("Origen",None)),
                    Estatus = m.Estatus.objects.get(idEstatus=request.POST.get("Estatus",None)),
                    fechaActualizacion = date.today(),
                    activo = True,
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
                    telcasa = request.POST.get("telcasa",None),
                    oficina = request.POST.get("oficina",None),
                    facebookid = request.POST.get("facebookid",None),
                )
                clientec.save()
                cl = contacto.save()
                direccion.save()
                return redirect('cliente:agregarCliente')

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
    else:
        raise PermissionDenied

@login_required(redirect_field_name='login:login')
def clientes(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.get(idAsesorCliente=idAsesorCliente)
        contacto = mLogin.Contacto.objects.filter(idpersona=asesorClientes.idCliente)
        direccion = mLogin.Direccion.objects.filter(idpersona=asesorClientes.idCliente)
        print(contacto)
        context = {
            "clientes":asesorClientes,
            "contactos":contacto,
            "direcciones":direccion,
        }
        return render(request,"cliente/cliente_show.html",context)
    else:
        raise PermissionDenied

@login_required(redirect_field_name='login:login')
def gestionarClientes(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        context = {
            "clientes":asesorClientes,
        }
        return render(request,"cliente/cliente_gestionar.html",context)
    else:
        raise PermissionDenied

@login_required(redirect_field_name='login:login')
def editar(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        editar = m.AsesorCliente.objects.get(idAsesorCliente=idAsesorCliente)
        if request.method == 'POST':
            usuario = f.UserForm(request.POST,instance=editar.idCliente.user)
            persona = f.PersonaForm(request.POST,instance=editar.idCliente)
            cliente = f.ClienteForm(request.POST,instance=editar)
            print(usuario.is_valid())
            print(request.POST)
            if usuario.is_valid():
                usuario.save()
                persona.save()
                cl = cliente.save()
                m.AsesorCliente.objects.filter(idAsesorCliente=cl.idAsesorCliente).update(
                    fechaActualizacion = date.today()
                )
                return redirect('cliente:gestionarCliente')
        else:
            usuario = f.UserForm(instance=editar.idCliente.user)
            persona = f.PersonaForm(instance=editar.idCliente)
            cliente = f.ClienteForm(instance=editar)
            context = {
                "usuario":usuario,
                "persona":persona,
                "cliente":cliente,
            }
            return render(request,"cliente/cliente_editar.html",context)
    else:
        raise PermissionDenied

@login_required(redirect_field_name='login:login')
def eliminar(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        eliminar = m.AsesorCliente.objects.get(idAsesorCliente=idAsesorCliente)
        m.AsesorCliente.objects.filter(idAsesorCliente=eliminar.idAsesorCliente).update(
            activo = False
        )
        return redirect('cliente:gestionarCliente')
    else:
        raise PermissionDenied
