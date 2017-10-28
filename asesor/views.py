from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models as mAsesor
from login import models as mLogin
from login import forms as f
from . import forms as fAesor
# Create your views here.

@login_required(redirect_field_name='login:login')
def agregarAsesor(request):
        if request.user.persona.idRol.idRole == 3:
            if request.method == 'POST':
                usuario = fLogin.UserForm(request.POST)
                persona = f.PersonaForm(request.POST)
                cliente = f.ClienteForm(request.POST)
                print(usuario.is_valid())
                print(request.POST)
                if usuario.is_valid() and persona.is_valid() and cliente.is_valid():
                    user = usuario.save()
                    rol = mLogin.Roles.objects.get(idRole=2)
                    fecha = request.POST.get("fechaDeNacimiento",None)
                    estadoCivil = request.POST.get("estadoCivil",None)
                    direccion = request.POST.get("idtipodireccion",None)
                    persona = mLogin.Persona.objects.get(user_id=user)
                    if estadoCivil == "":
                        estado = mLogin.EstadoCivil.objects.get(idEstadoCivil="1")
                    else:
                        estado = mLogin.EstadoCivil.objects.get(idEstadoCivil=estadoCivil)
                    if direccion == "":
                        tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion="1")
                    else:
                        tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion=direccion)

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
                    contacto.save()
                    direccion.save()
                    return redirect('asesor:gestionarAsesor')
                else:
                    return redirect('asesor:agregarAsesor')
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
            return render(request,"asesor/cliente_add.html",context)
        else:
            return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def editarAsesor(request):
    return render()

@login_required(redirect_field_name='login:login')
def eliminarAsesor(request):
    return render()

@login_required(redirect_field_name='login:login')
def gestionarAsesor(request):
    if request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        context = {
            "clientes":asesorClientes,
        }
        return render(request,"cliente/cliente_gestionar.html",context)
    else:
        return render(request,'error/404.html')
